from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from django.http import HttpResponse
from datetime import date
from .models import Loyer, Paiement, Bordereau
from .serializers import LoyerSerializer, PaiementSerializer, BordereauSerializer

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
    
    # ✅ Filtres
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
    
    # ✅ Filtres
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
    badge_label = '✅ SOLDÉ' if solde <= 0 else '⚠️ PARTIEL'

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
  /* Force la suppression des headers/footers navigateur */
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

/* ── bouton impression (disparaît à l'impression) ── */
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

/* ── en-tête ── */
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

/* ── lignes info ── */
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

/* ── tableau paiements ── */
table {{ width: 100%; border-collapse: collapse; margin: 3px 0; }}
th {{ font-size: 9px; color: #555; text-align: left; border-bottom: 1px solid #ccc; padding-bottom: 2px; }}
td {{ font-size: 10px; padding: 1px 0; }}
td.r {{ text-align: right; }}

/* ── totaux ── */
.totals .row {{ margin: 2px 0; }}
.totals .paye {{ color: #10b981; }}
.totals .solde {{ color: {solde_color}; font-size: 12px; }}

/* ── signature ── */
.sig {{
  margin-top: 8px;
  text-align: center;
  border: 1px dashed #ccc;
  border-radius: 4px;
  padding: 5px;
}}
.sig .sig-lbl  {{ font-size: 9px; color: #777; }}
.sig .sig-name {{ font-size: 11px; font-weight: 700; margin-top: 12px; }}
.sig .sig-sub  {{ font-size: 9px; color: #aaa; }}

/* ── pied ── */
.foot {{ text-align: center; font-size: 9px; color: #aaa; margin-top: 6px; }}

/* ── filigrane ── */
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

<div class="sig">
  <div class="sig-lbl">L'Administrateur</div>
  <div style="height:18px"></div>
  <div class="sig-name">ADEXPERT</div>
  <div class="sig-sub">(Signature &amp; Cachet)</div>
<p class="foot">Émis le {date.today().strftime('%d/%m/%Y')} — Document officiel ADEXPERT</p>
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
class BordereauListView(generics.ListAPIView):
    serializer_class = BordereauSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self): return Bordereau.objects.all().order_by('-created_at')

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def valider_bordereau(request, pk):
    try:
        b = Bordereau.objects.get(pk=pk)
    except Bordereau.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)
    b.statut = request.data.get('statut','valide')
    b.commentaire_admin = request.data.get('commentaire','')
    b.save()
    return Response(BordereauSerializer(b).data)
