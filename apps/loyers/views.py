from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from django.http import HttpResponse
from datetime import date
from .models import Loyer, Paiement, Bordereau
from .serializers import LoyerSerializer, PaiementSerializer, BordereauSerializer
import json
class LoyerListCreate(generics.ListCreateAPIView):
    serializer_class = LoyerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        qs = Loyer.objects.select_related('locataire', 'local', 'contrat')
        
        # Filtres rôle
        if user.role == 'locataire' and user.locataire_profile:
            qs = qs.filter(locataire=user.locataire_profile)
        elif user.role == 'proprietaire' and user.proprietaire_profile:
            qs = qs.filter(local__proprietaire=user.proprietaire_profile)
        
        # ✅ Filtres dashboard (admin/gestionnaire)
        proprietaire_id = self.request.query_params.get('proprietaire')
        immeuble_id = self.request.query_params.get('immeuble')
        
        if proprietaire_id:
            qs = qs.filter(local__proprietaire_id=proprietaire_id)
        if immeuble_id:
            qs = qs.filter(local__immeuble_id=immeuble_id)
        
        return qs
class LoyerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loyer.objects.all()
    serializer_class = LoyerSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def loyers_en_retard(request):
    qs = Loyer.objects.filter(statut='retard')
    user = request.user

    # ✅ Filtre automatique si l'utilisateur est un propriétaire
    if user.role == 'proprietaire' and user.proprietaire_profile:
        qs = qs.filter(local__proprietaire=user.proprietaire_profile)
    elif user.role == 'locataire' and user.locataire_profile:
        qs = qs.filter(locataire=user.locataire_profile)

    # Filtres dashboard (admin/gestionnaire)
    proprietaire_id = request.query_params.get('proprietaire')
    immeuble_id = request.query_params.get('immeuble')
    if proprietaire_id:
        qs = qs.filter(local__proprietaire_id=proprietaire_id)
    if immeuble_id:
        qs = qs.filter(local__immeuble_id=immeuble_id)

    return Response(LoyerSerializer(qs, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def loyers_impayes(request):
    qs = Loyer.objects.filter(statut__in=['attente', 'partiel'])
    user = request.user

    # Filtre automatique si l'utilisateur est un propriétaire
    if user.role == 'proprietaire' and user.proprietaire_profile:
        qs = qs.filter(local__proprietaire=user.proprietaire_profile)
    elif user.role == 'locataire' and user.locataire_profile:
        qs = qs.filter(locataire=user.locataire_profile)

    # Filtres dashboard (admin/gestionnaire)
    proprietaire_id = request.query_params.get('proprietaire')
    immeuble_id = request.query_params.get('immeuble')
    if proprietaire_id:
        qs = qs.filter(local__proprietaire_id=proprietaire_id)
    if immeuble_id:
        qs = qs.filter(local__immeuble_id=immeuble_id)

    return Response(LoyerSerializer(qs, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def loyers_paiements_annules(request):
    qs = Loyer.objects.filter(paiements__annule=True).distinct()
    user = request.user

    # Filtre automatique si l'utilisateur est un propriétaire
    if user.role == 'proprietaire' and user.proprietaire_profile:
        qs = qs.filter(local__proprietaire=user.proprietaire_profile)
    elif user.role == 'locataire' and user.locataire_profile:
        qs = qs.filter(locataire=user.locataire_profile)

    # Filtres dashboard (admin/gestionnaire)
    proprietaire_id = request.query_params.get('proprietaire')
    immeuble_id = request.query_params.get('immeuble')
    if proprietaire_id:
        qs = qs.filter(local__proprietaire_id=proprietaire_id)
    if immeuble_id:
        qs = qs.filter(local__immeuble_id=immeuble_id)

    return Response(LoyerSerializer(qs, many=True).data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enregistrer_paiement(request, pk):
    try:
        loyer = Loyer.objects.get(pk=pk)
    except Loyer.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)
    montant = request.data.get('montant')
    if not montant or float(montant) <= 0:
        return Response({'error': 'Montant invalide.'}, status=400)
    paiement = Paiement.objects.create(
        loyer=loyer, montant=montant,
        date_paiement=request.data.get('date_paiement', timezone.now().date()),
        mode_paiement=request.data.get('mode_paiement','especes'),
        reference=request.data.get('reference',''), created_by=request.user)
    try:
        from apps.notifications.models import Notification
        Notification.objects.create(
            destinataire_locataire=loyer.locataire,
            titre='✅ Paiement enregistré',
            message=f'Votre paiement de {float(paiement.montant):,.0f} BIF pour «{loyer.libelle}» a été enregistré le {paiement.date_paiement.strftime("%d/%m/%Y")}. Solde restant : {float(loyer.solde_restant):,.0f} BIF.',
            type_notif='paiement')
    except Exception:
        pass
    return Response({'detail': 'Paiement enregistré.', 'loyer': LoyerSerializer(loyer).data})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lister_paiements_loyer(request, pk):
    try:
        loyer = Loyer.objects.get(pk=pk)
    except Loyer.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)
    data = [{
        'id': p.id,
        'montant': float(p.montant),
        'date_paiement': p.date_paiement,
        'mode_paiement': p.get_mode_paiement_display(),
        'reference': p.reference,
        'annule': p.annule,
        'date_annulation': p.date_annulation,
        'annule_par': p.annule_par.username if p.annule_par else None,
        'motif_annulation': p.motif_annulation,
    } for p in loyer.paiements.filter(annule=False).order_by('-date_paiement')]
    return Response(data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def annuler_paiement(request, pk):
    from apps.notifications.models import Notification  # adapte le chemin d'import si besoin

    if not (request.user.role in ('admin', 'gestionnaire')):
        return Response({'error': 'Accès réservé aux admins/gestionnaires.'}, status=403)
    try:
        paiement = Paiement.objects.select_related('loyer', 'loyer__locataire').get(pk=pk)
    except Paiement.DoesNotExist:
        return Response({'error': 'Paiement introuvable.'}, status=404)
    if paiement.annule:
        return Response({'error': 'Ce paiement est déjà annulé.'}, status=400)

    paiement.annule = True
    paiement.date_annulation = timezone.now()
    paiement.annule_par = request.user
    paiement.motif_annulation = request.data.get('motif', '')
    paiement.save(update_fields=['annule', 'date_annulation', 'annule_par', 'motif_annulation'])

    paiement.loyer.update_statut()

    # ✅ Notifier le locataire
    Notification.objects.create(
        destinataire_locataire=paiement.loyer.locataire,
        loyer=paiement.loyer,
        titre='Paiement annulé',
        message=f"Votre paiement de {paiement.montant} BIF du {paiement.date_paiement} pour le loyer "
                f"« {paiement.loyer.libelle} » a été annulé"
                f"{' — Motif : ' + paiement.motif_annulation if paiement.motif_annulation else ''}. "
                f"Merci de soumettre un nouveau bordereau.",
        type_notif='paiement',
    )

    return Response({'message': 'Paiement annulé avec succès.'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def quittance_html(request, pk):
    try:
        loyer = Loyer.objects.get(pk=pk)
    except Loyer.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)

    paye = float(loyer.montant_paye)
    total = float(loyer.montant_total)
    solde = total - paye
    rows = ''.join(
        f'<tr><td>{p.date_paiement.strftime("%d/%m/%Y")}</td>'
        f'<td>{p.get_mode_paiement_display()}</td>'
        f'<td class="r"><b>{float(p.montant):,.0f}</b></td></tr>'
        for p in loyer.paiements.all()
    )
    solde_color = '#10b981' if solde <= 0 else '#ef4444'
    badge_bg    = '#d1fae5' if solde <= 0 else '#fef3c7'
    badge_color = '#065f46' if solde <= 0 else '#78350f'
    badge_label = '✅ CONFIRMÉ' if solde <= 0 else '⚠️ PARTIEL'

    # ── QR code : nom locataire, montant payé, référence bancaire ──
    dernier_paiement = loyer.paiements.order_by('-date_paiement').first()
    if dernier_paiement:
        banque_ref = dernier_paiement.reference or dernier_paiement.get_mode_paiement_display()
    else:
        banque_ref = '—'
        
    verification_path = request.build_absolute_uri(f'/api/loyers/{loyer.id}/verifier-quittance/')
    qr_content = verification_path
    from urllib.parse import quote
    qr_content_url = quote(qr_content)

    html = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8">
<title>Quittance — {loyer.locataire_nom}</title>
<style>
@page {{ size: 80mm auto; margin: 4mm; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}

@page {{
  size: 80mm auto;
  margin: 4mm;
  margin-top: 0;
  margin-bottom: 0;
}}
@media print {{
  html, body {{
    margin: 0 !important;
    padding: 0 !important;
  }}
  .btn-print {{ display: none !important; }}
  head title {{ display: none; }}
}}
body {{
  font-family: 'Courier New', monospace;
  font-size: 11px;
  width: 72mm;
  margin: 0 auto;
  background: #fff;
  color: #111;
}}

.btn-print {{
  display: block;
  width: 100%;
  margin-bottom: 6px;
  padding: 7px;
  background: #1e40af;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}}
.btn-print:hover {{ background: #1d3799; }}

.hd {{ text-align: center; border-bottom: 1px dashed #555; padding-bottom: 5px; margin-bottom: 5px; }}
.hd h1 {{ font-size: 13px; font-weight: 800; color: #1e40af; }}
.hd p  {{ font-size: 9px; color: #555; margin-top: 1px; }}
.badge {{
  display: inline-block;
  margin-top: 3px;
  padding: 1px 8px;
  border-radius: 20px;
  font-size: 10px;
  font-weight: 700;
  background: {badge_bg};
  color: {badge_color};
}}

.sep {{ border: none; border-top: 1px dashed #aaa; margin: 5px 0; }}
.row {{ display: flex; justify-content: space-between; margin: 2px 0; }}
.row .lbl {{ color: #555; }}
.row .val {{ font-weight: 700; }}
.section-title {{
  font-size: 9px;
  text-transform: uppercase;
  color: #94a3b8;
  font-weight: 700;
  margin: 4px 0 2px;
  letter-spacing: .5px;
}}

table {{ width: 100%; border-collapse: collapse; margin: 3px 0; }}
th {{ font-size: 9px; color: #555; text-align: left; border-bottom: 1px solid #ccc; padding-bottom: 2px; }}
td {{ font-size: 10px; padding: 1px 0; }}
td.r {{ text-align: right; }}

.totals .row {{ margin: 2px 0; }}
.totals .paye {{ color: #10b981; }}
.totals .solde {{ color: {solde_color}; font-size: 12px; }}

/* ── bloc QR (remplace la signature) ── */
.qr-box {{
  margin-top: 8px;
  text-align: center;
  border: 1px dashed #ccc;
  border-radius: 4px;
  padding: 8px;
}}
.qr-lbl {{ font-size: 9px; color: #777; margin-bottom: 4px; }}
.qr-sub {{ font-size: 8.5px; color: #aaa; margin-top: 4px; }}

.foot {{ text-align: center; font-size: 9px; color: #aaa; margin-top: 6px; }}

.wm {{
  position: fixed; top: 38%; left: 2%;
  opacity: .04; font-size: 38px; font-weight: 900;
  transform: rotate(-35deg); color: #1e40af;
  pointer-events: none; white-space: nowrap;
}}

@media print {{
  .btn-print {{ display: none !important; }}
  body {{ width: 72mm; }}
}}
</style></head><body>

<div class="wm">ADEXPERT</div>

<button class="btn-print" onclick="window.print()">🖨️ Imprimer / Télécharger PDF</button>

<div class="hd">
  <h1><div class="logo-icon">&#127962;</div> ADEXPERT</h1>
  <p>Quittance de Loyer — Bujumbura, Burundi</p>
  <span class="badge">{badge_label}</span>
</div>

<div class="section-title">Locataire &amp; Local</div>
<div class="row"><span class="lbl">Locataire</span><span class="val">{loyer.locataire_nom}</span></div>
<div class="row"><span class="lbl">Local</span><span class="val">{loyer.local_reference}</span></div>
<div class="row"><span class="lbl">Période</span><span class="val">{loyer.libelle}</span></div>
<div class="row"><span class="lbl">Échéance</span><span class="val">{loyer.echeance.strftime('%d/%m/%Y')}</span></div>

{'<hr class="sep"><div class="section-title">Paiements</div><table><thead><tr><th>Date</th><th>Mode</th><th style="text-align:right">Montant (BIF)</th></tr></thead><tbody>' + rows + '</tbody></table>' if rows else ''}

<hr class="sep">
<div class="section-title">Récapitulatif</div>
<div class="totals">
  <div class="row"><span class="lbl">Loyer HC</span><span class="val">{float(loyer.loyer_hors_charges):,.0f} BIF</span></div>
  <div class="row"><span class="lbl">Charges</span><span class="val">{float(loyer.charges):,.0f} BIF</span></div>
  <div class="row"><span class="lbl"><b>Total</b></span><span class="val"><b>{total:,.0f} BIF</b></span></div>
  <hr class="sep">
  <div class="row paye"><span class="lbl">Payé</span><span class="val">{paye:,.0f} BIF</span></div>
  <div class="row solde"><span class="lbl"><b>Solde</b></span><span class="val"><b>{solde:,.0f} BIF</b></span></div>
</div>
<div class="qr-box">
  <div class="qr-lbl">Vérification d'authenticité</div>
  <div style="display:flex;justify-content:center;margin:4px 0">
    <img src="https://api.qrserver.com/v1/create-qr-code/?size=100x100&data={qr_content_url}" width="90" height="90" alt="QR Code">
  </div>
  <div class="qr-sub">Scannez pour vérifier ce paiement</div>
</div>

<p class="foot">Émis le {date.today().strftime('%d/%m/%Y')} — Document officiel ADEXPERT</p>


</body></html>"""
    return HttpResponse(html, content_type='text/html; charset=utf-8')

from django.shortcuts import render
from rest_framework.decorators import permission_classes as drf_permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def verifier_quittance(request, pk):
    try:
        loyer = Loyer.objects.get(pk=pk)
    except Loyer.DoesNotExist:
        html = """<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vérification — Introuvable</title>
<style>
body{font-family:'Segoe UI',sans-serif;background:#f1f5f9;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0}
.card{background:#fff;border-radius:16px;padding:32px 28px;max-width:360px;width:100%;box-shadow:0 8px 30px rgba(0,0,0,.1);text-align:center}
.logo{font-size:20px;font-weight:800;color:#1e40af;margin-bottom:4px}
.sub{font-size:12px;color:#64748b;margin-bottom:20px}
.badge{display:inline-block;padding:8px 18px;border-radius:30px;font-weight:700;font-size:14px;background:#fee2e2;color:#991b1b;margin-bottom:14px}
.msg{font-size:13px;color:#475569;line-height:1.6}
</style></head><body>
<div class="card">
  <div class="logo">🏛️ ADEXPERT</div>
  <div class="sub">Vérification de quittance</div>
  <div class="badge">❌ INTROUVABLE</div>
  <div class="msg">Ce document n'est pas reconnu par ADEXPERT. Il ne correspond à aucun paiement enregistré dans notre système.</div>
</div>
</body></html>"""
        return HttpResponse(html, content_type='text/html; charset=utf-8')

    paye = float(loyer.montant_paye)
    total = float(loyer.montant_total)
    solde = total - paye
    statut_label = 'Soldé' if solde <= 0 else 'Partiel'
    badge_bg = '#d1fae5' if solde <= 0 else '#fef3c7'
    badge_color = '#065f46' if solde <= 0 else '#78350f'
    now_str = timezone.now().strftime('%d/%m/%Y à %Hh%M')

    html = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vérification — Quittance ADEXPERT</title>
<style>
body{{font-family:'Segoe UI',sans-serif;background:#f1f5f9;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0;padding:20px}}
.card{{background:#fff;border-radius:16px;padding:32px 28px;max-width:380px;width:100%;box-shadow:0 8px 30px rgba(0,0,0,.1)}}
.logo{{font-size:20px;font-weight:800;color:#1e40af;text-align:center;margin-bottom:4px}}
.sub{{font-size:12px;color:#64748b;text-align:center;margin-bottom:18px}}
.badge-wrap{{text-align:center;margin-bottom:18px}}
.badge{{display:inline-block;padding:8px 18px;border-radius:30px;font-weight:700;font-size:14px;background:{badge_bg};color:{badge_color}}}
.desc{{font-size:12.5px;color:#475569;line-height:1.6;margin-bottom:18px;text-align:center}}
.row{{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f1f5f9;font-size:13px}}
.row .lbl{{color:#94a3b8}}
.row .val{{font-weight:700;color:#0f172a}}
.foot{{text-align:center;font-size:10.5px;color:#94a3b8;margin-top:18px}}
</style></head><body>
<div class="card">
  <div class="logo">🏛️ ADEXPERT</div>
  <div class="sub">Vérification de quittance</div>
  <div class="badge-wrap"><span class="badge">✅ QUITTANCE AUTHENTIQUE</span></div>
  <div class="desc">Cette quittance a été émise par ADEXPERT et correspond à un paiement enregistré dans notre système.</div>
  <div class="row"><span class="lbl">Locataire</span><span class="val">{loyer.locataire_nom}</span></div>
  <div class="row"><span class="lbl">Local</span><span class="val">{loyer.local_reference}</span></div>
  <div class="row"><span class="lbl">Montant payé</span><span class="val">{paye:,.0f} BIF</span></div>
  <div class="row"><span class="lbl">Statut</span><span class="val">{statut_label}</span></div>
  <div class="foot">Vérifié le {now_str}</div>
</div>
</body></html>"""
    return HttpResponse(html, content_type='text/html; charset=utf-8')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rapport_mensuel_loyers(request):
    mois = int(request.query_params.get('mois', timezone.now().month))
    annee = int(request.query_params.get('annee', timezone.now().year))
    qs = Loyer.objects.filter(echeance__month=mois, echeance__year=annee)
    # ✅ Filtre propriétaire
    user = request.user
    if user.role == 'proprietaire' and user.proprietaire_profile:
        qs = qs.filter(local__proprietaire=user.proprietaire_profile)
    total = qs.count(); payes = qs.filter(statut='paye').count(); retard = qs.filter(statut='retard').count()
    enc = sum(float(l.montant_paye) for l in qs); imp = sum(float(l.solde_restant) for l in qs)
    return Response({'total_loyers':total,'loyers_payes':payes,'loyers_retard':retard,
        'taux_paiement':round(payes/total*100,1) if total else 0,'montant_encaisse':enc,'montant_impaye':imp})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rapport_journalier(request):
    d = request.query_params.get('date', str(timezone.now().date()))
    paiements = Paiement.objects.filter(date_paiement=d)
    # ✅ Filtre propriétaire
    user = request.user
    if user.role == 'proprietaire' and user.proprietaire_profile:
        paiements = paiements.filter(loyer__local__proprietaire=user.proprietaire_profile)
    rep = {}
    for p in paiements:
        k = p.get_mode_paiement_display()
        rep[k] = rep.get(k, 0) + float(p.montant)
    return Response({'date':d,'nombre_paiements':paiements.count(),'total_encaisse':sum(float(p.montant) for p in paiements),'repartition_par_mode':rep})
# class BordereauListView(generics.ListAPIView):
#     serializer_class = BordereauSerializer
#     permission_classes = [IsAuthenticated]
#     def get_queryset(self): return Bordereau.objects.all().order_by('-created_at')


# APRÈS
import re
UUID_RE = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.IGNORECASE)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bordereau_list(request):
    from django.db import connection
    statut = request.query_params.get('statut')
    
    query = "SELECT id, locataire_id, loyer_id, photo, notes, statut, commentaire_admin, created_at FROM loyers_bordereau"
    params = []
    if statut:
        query += " WHERE statut = %s"
        params.append(statut)
    query += " ORDER BY created_at DESC"
    
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    
    results = []
    for row in rows:
        b = dict(zip(columns, row))
        try:
            from apps.locataires.models import Locataire
            loc = Locataire.objects.get(pk=b['locataire_id'])
            b['locataire_nom'] = loc.nom_prenom
        except Exception:
            b['locataire_nom'] = '—'
        try:
            from apps.loyers.models import Loyer
            loyer = Loyer.objects.get(pk=b['loyer_id']) if b['loyer_id'] else None
            b['loyer_libelle'] = loyer.libelle if loyer else '—'
        except Exception:
            b['loyer_libelle'] = '—'

        # Construire photo_url correctement
        raw = b.get('photo', '') or ''
        if not raw:
            b['photo_url'] = None
        else:
            match = UUID_RE.search(raw)
            if match:
                b['photo_url'] = f'https://2uw2o5rfke.ucarecd.net/{match.group(0)}/'
            else:
                b['photo_url'] = None

        b['created_at'] = str(b['created_at'])
        results.append(b)
    
    return Response(results)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def envoyer_quittance(request, pk):
    try:
        loyer = Loyer.objects.get(pk=pk)
    except Loyer.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)

    if float(loyer.montant_paye) <= 0:
        return Response({'error': 'Aucun paiement enregistré pour ce loyer.'}, status=400)

    loyer.quittance_envoyee = True
    loyer.save(update_fields=['quittance_envoyee'])

    try:
        from apps.notifications.models import Notification
        Notification.objects.create(
            destinataire_locataire=loyer.locataire,
            loyer=loyer,
            titre='🧾 Quittance disponible',
            message=f'La quittance de votre loyer «{loyer.libelle}» ({loyer.local_reference}) a été générée par l\'administration. Cliquez ici pour la télécharger.',
            type_notif='paiement'
        )
    except Exception as e:
        return Response({'error': f'Erreur lors de la notification : {e}'}, status=500)

    return Response({'detail': 'Quittance envoyée au locataire.'})



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def valider_bordereau(request, pk):
    try:
        b = Bordereau.objects.get(pk=pk)
    except Bordereau.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)

    nouveau_statut = request.data.get('statut', 'valide')
    b.statut = nouveau_statut
    b.commentaire_admin = request.data.get('commentaire', '')
    b.save()

    if nouveau_statut == 'valide' and b.loyer_id:
        loyer = b.loyer
        ref = b.numero
        deja_paye = Paiement.objects.filter(loyer=loyer, reference=ref, annule=False).exists()
        if not deja_paye and loyer.solde_restant > 0:
            Paiement.objects.create(
                loyer=loyer,
                montant=loyer.solde_restant,
                date_paiement=timezone.now().date(),
                mode_paiement='autre',
                reference=ref,
                reference_transaction=b.reference_client,  # ✅ transmet la réf. saisie par le locataire
                statut_validation='valide',
                date_validation=timezone.now(),
                created_by=request.user,
                validated_by=request.user,
            )

    return Response(BordereauSerializer(b).data)