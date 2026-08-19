from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Locataire
from .serializers import LocataireSerializer

class LocataireListCreate(generics.ListCreateAPIView):
    serializer_class = LocataireSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.role == 'locataire' and user.locataire_profile:
            return Locataire.objects.filter(pk=user.locataire_profile.pk)
             # ✅ Filtre par propriétaire
        if user.role == 'proprietaire' and user.proprietaire_profile:
            return Locataire.objects.filter(
                contrats__local__proprietaire=user.proprietaire_profile
            ).distinct()
        return Locataire.objects.all()
        

class LocataireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer
    permission_classes = [IsAuthenticated]
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def locataire_historique(request, pk):
    from apps.loyers.models import Loyer, Paiement

    is_proprietaire = request.user.role == 'proprietaire' and not request.user.is_superuser

    loyers = Loyer.objects.filter(locataire_id=pk).order_by('-echeance')
    data = []
    for loyer in loyers:
        item = {
            'loyer_id': loyer.id, 'libelle': loyer.libelle,
            'periode_debut': loyer.periode_debut, 'periode_fin': loyer.periode_fin,
            'montant_total': float(loyer.montant_total), 'montant_paye': float(loyer.montant_paye),
            'solde_restant': float(loyer.solde_restant), 'statut': loyer.statut,
            'statut_display': loyer.get_statut_display_custom(), 'echeance': loyer.echeance,
        }
        if is_proprietaire:
            item['paiements'] = []
        else:
            item['paiements'] = list(Paiement.objects.filter(loyer=loyer, annule=False).values(
                'montant', 'date_paiement', 'mode_paiement', 'reference'
            ))
        data.append(item)

    loyers_payes = len([d for d in data if d['solde_restant'] <= 0])

    return Response({'locataire_id': pk, 'historique': data,
        'total_loyers': len(data),
        'loyers_payes': loyers_payes,
        'loyers_restants': len(data) - loyers_payes,
        'montant_total_du': sum(d['montant_total'] for d in data),
        'montant_total_paye': sum(d['montant_paye'] for d in data),
        'montant_total_restant': sum(d['solde_restant'] for d in data)})
    # @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def upload_bordereau(request, pk):
#     from apps.loyers.models import Bordereau
#     photo_uuid = request.data.get('photo')
#     if not photo_uuid:
#         return Response({'error': 'Photo requise.'}, status=400)
#     b = Bordereau.objects.create(
#         locataire_id=pk,
#         loyer_id=request.data.get('loyer_id'),
#         photo=photo_uuid,
#         notes=request.data.get('notes', ''),
#         statut='en_attente'
#     )
#     return Response({'id': b.id, 'statut': b.statut}, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_bordereau(request, pk):
    from apps.loyers.models import Bordereau
    import re
    photo_uuid = request.data.get('photo')
    if not photo_uuid:
        return Response({'error': 'Photo requise.'}, status=400)
    
    # Extraire uniquement l'UUID si une URL complète est envoyée
    uuid_match = re.search(
        r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        str(photo_uuid), re.IGNORECASE
    )
    if uuid_match:
        photo_uuid = uuid_match.group(0)
    
    b = Bordereau.objects.create(
        locataire_id=pk,
        loyer_id=request.data.get('loyer_id'),
        photo=photo_uuid,
        notes=request.data.get('notes', ''),
        statut='en_attente'
    )
    return Response({'id': b.id, 'statut': b.statut}, status=201)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_bordereaux(request, pk):
    from apps.loyers.models import Bordereau
    from apps.loyers.serializers import BordereauSerializer
    bs = Bordereau.objects.filter(locataire_id=pk).order_by('-created_at')
    return Response(BordereauSerializer(bs, many=True, context={'request':request}).data)

# ── PDF Historique locataire (ReportLab, non modifiable) ──
from datetime import datetime, date as date_cls
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    Image, SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
)
import os
from django.conf import settings
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def locataire_historique_pdf(request, pk):
    from apps.loyers.models import Loyer, Paiement

    try:
        locataire = Locataire.objects.get(pk=pk)
    except Locataire.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)

    user = request.user
    is_proprietaire = user.role == 'proprietaire' and not user.is_superuser

    # ── Sécurité : vérifie que l'utilisateur a le droit de voir ce locataire ──
    if user.role == 'proprietaire' and user.proprietaire_profile:
        autorise = Locataire.objects.filter(
            pk=pk, contrats__local__proprietaire=user.proprietaire_profile
        ).exists()
        if not autorise:
            return Response({'error': 'Non autorisé.'}, status=403)
    elif user.role == 'locataire':
        if not user.locataire_profile or user.locataire_profile.pk != int(pk):
            return Response({'error': 'Non autorisé.'}, status=403)

    # ── Filtrage par période ──
    loyers = Loyer.objects.filter(locataire_id=pk).order_by('echeance')

    mois = request.GET.get('mois')
    annee = request.GET.get('annee')
    date_debut = request.GET.get('date_debut')
    date_fin = request.GET.get('date_fin')

    periode_label = "Historique complet"
    if mois and annee:
        loyers = loyers.filter(echeance__month=int(mois), echeance__year=int(annee))
        mois_noms = ['', 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
                     'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        periode_label = f"{mois_noms[int(mois)]} {annee}"
    elif date_debut and date_fin:
        loyers = loyers.filter(echeance__gte=date_debut, echeance__lte=date_fin)
        d1 = datetime.strptime(date_debut, '%Y-%m-%d').strftime('%d/%m/%Y')
        d2 = datetime.strptime(date_fin, '%Y-%m-%d').strftime('%d/%m/%Y')
        periode_label = f"Du {d1} au {d2}"

    if not loyers.exists():
        return Response({'error': 'Aucun loyer sur cette période.'}, status=404)

    # ── Construction du PDF ──
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        topMargin=18 * mm, bottomMargin=16 * mm,
        leftMargin=16 * mm, rightMargin=16 * mm,
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title2', parent=styles['Heading1'],
                                  fontSize=16, textColor=colors.HexColor('#1e40af'),
                                  alignment=1)  # 1 = centré
    sub_style = ParagraphStyle('Sub', parent=styles['Normal'],
                                fontSize=10, textColor=colors.HexColor('#555555'),
                                alignment=1)  # centré
    cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=8, leading=10)

    elems = []

    # ── En-tête avec logos (Burundi à gauche, ADEXPERT à droite) ──
    logo_burundi_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'armoiries_burundi.png')
    logo_adexpert_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'logo_adexpert.png')

    logo_bi = Image(logo_burundi_path, width=20 * mm, height=20 * mm) if os.path.exists(logo_burundi_path) else Paragraph('', sub_style)
    logo_ax = Image(logo_adexpert_path, width=20 * mm, height=20 * mm) if os.path.exists(logo_adexpert_path) else Paragraph('', sub_style)

    titre_central = [
        Paragraph("ADEXPERT — Historique de paiements", title_style),
        Paragraph(f"Locataire : <b>{locataire.nom_prenom}</b>", sub_style),
        Paragraph(f"Période : {periode_label}", sub_style),
        Paragraph(f"Généré le {date_cls.today().strftime('%d/%m/%Y')}", sub_style),
    ]

    header_table = Table(
        [[logo_bi, titre_central, logo_ax]],
        colWidths=[24 * mm, 130 * mm, 24 * mm],
    )
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ]))
    elems.append(header_table)
    elems.append(Spacer(1, 8 * mm))

    # ── Colonnes conditionnelles selon le rôle ──
    if is_proprietaire:
        header = ['Libellé', 'Échéance', 'Total (BIF)', 'Payé (BIF)', 'Solde (BIF)', 'Statut', 'Paiements']
        col_widths = [30*mm, 22*mm, 24*mm, 24*mm, 24*mm, 20*mm, 34*mm]
    else:
        header = ['Libellé', 'Échéance', 'Total (BIF)', 'Payé (BIF)', 'Solde (BIF)', 'Statut', 'N° Bordereau', 'Validation', 'Paiements']
        col_widths = [20*mm, 16*mm, 18*mm, 18*mm, 18*mm, 14*mm, 20*mm, 18*mm, 36*mm]

    data = [header]

    total_du = total_paye = total_solde = 0
    for loyer in loyers:
        total_du += float(loyer.montant_total)
        total_paye += float(loyer.montant_paye)
        total_solde += float(loyer.solde_restant)

        if is_proprietaire:
            paiements_txt = '—'
            row = [
                Paragraph(loyer.libelle, cell_style),
                loyer.echeance.strftime('%d/%m/%Y'),
                f"{float(loyer.montant_total):,.0f}",
                f"{float(loyer.montant_paye):,.0f}",
                f"{float(loyer.solde_restant):,.0f}",
                loyer.get_statut_display_custom(),
                Paragraph(paiements_txt, cell_style),
            ]
        else:
            pays = Paiement.objects.filter(loyer=loyer, annule=False)

            paiements_txt = '<br/>'.join(
                f"{p.date_paiement.strftime('%d/%m/%Y')} — {float(p.montant):,.0f} ({p.get_mode_paiement_display()})"
                for p in pays
            ) or '—'

            # ── N° de bordereau (référence) : preuve de paiement, évite toute contestation ──
            bordereaux_txt = '<br/>'.join(
                (p.reference or '—') for p in pays
            ) or '—'

            # ── Statut de validation : un paiement "En attente" n'est pas encore confirmé ──
            validation_txt = '<br/>'.join(
                p.get_statut_validation_display() for p in pays
            ) or '—'

            row = [
                Paragraph(loyer.libelle, cell_style),
                loyer.echeance.strftime('%d/%m/%Y'),
                f"{float(loyer.montant_total):,.0f}",
                f"{float(loyer.montant_paye):,.0f}",
                f"{float(loyer.solde_restant):,.0f}",
                loyer.get_statut_display_custom(),
                Paragraph(bordereaux_txt, cell_style),
                Paragraph(validation_txt, cell_style),
                Paragraph(paiements_txt, cell_style),
            ]

        data.append(row)

    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.hAlign = 'CENTER'
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    elems.append(table)
    elems.append(Spacer(1, 8 * mm))

    solde_color = colors.HexColor('#10b981') if total_solde <= 0 else colors.HexColor('#ef4444')
    recap = Table([
        ['Total dû', 'Total payé', 'Solde restant'],
        [f"{total_du:,.0f} BIF", f"{total_paye:,.0f} BIF", f"{total_solde:,.0f} BIF"],
    ], colWidths=[57*mm, 57*mm, 58*mm])
    recap.hAlign = 'CENTER'
    recap.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#eef1f8')),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TEXTCOLOR', (2, 1), (2, 1), solde_color),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    elems.append(recap)

    # ── Signature de l'admin ADEXPERT ──
    elems.append(Spacer(1, 12 * mm))

    signature_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'signature_admin.png')

    sign_style = ParagraphStyle('Sign', parent=styles['Normal'], fontSize=9,
                                 alignment=2)  # 2 = droite
    sign_label_style = ParagraphStyle('SignLabel', parent=styles['Normal'], fontSize=8,
                                       textColor=colors.HexColor('#555555'), alignment=2)

    if os.path.exists(signature_path):
        sign_block = [
            Image(signature_path, width=35 * mm, height=15 * mm),
            Paragraph("L'Administrateur D'ADEXPERT", sign_label_style),
        ]
    else:
        sign_block = [
            Spacer(1, 10 * mm),
            Paragraph("_____________________________", sign_style),
            Paragraph("L'Administrateur D'ADEXPERT", sign_label_style),
        ]

    signature_table = Table(
        [[Paragraph('', cell_style), sign_block]],
        colWidths=[110 * mm, 60 * mm],
    )
    signature_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
    ]))
    elems.append(signature_table)

    doc.build(elems)
    buffer.seek(0)

    filename = f"historique_{locataire.nom_prenom.replace(' ', '_')}_{date_cls.today().isoformat()}.pdf"
    response = HttpResponse(buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response