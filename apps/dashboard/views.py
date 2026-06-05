from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    from apps.locaux.models import Local
    from apps.loyers.models import Loyer
    from apps.charges.models import Charge
    from dateutil.relativedelta import relativedelta

    user = request.user
    today = timezone.now().date()
    m, y = today.month, today.year

    lqs   = Local.objects.all()
    loyqs = Loyer.objects.all()
    chqs  = Charge.objects.all()

    is_proprio = (user.role == 'proprietaire' and user.proprietaire_profile is not None)
    if is_proprio:
        p = user.proprietaire_profile
        lqs   = lqs.filter(proprietaire=p)
        loyqs = loyqs.filter(local__proprietaire=p)
        chqs  = chqs.filter(local__proprietaire=p)

    total  = lqs.count()
    occ    = sum(1 for l in lqs if l.est_occupe)
    lm     = loyqs.filter(echeance__month=m, echeance__year=y)
    rev    = sum(float(l.montant_paye) for l in lm)
    ch     = sum(float(c.montant_ttc) for c in chqs.filter(date_charge__month=m, date_charge__year=y))
    payes  = lm.filter(statut='paye').count()
    retard = lm.filter(statut='retard').count()
    taux   = round(payes / lm.count() * 100, 1) if lm.count() else 0

    evo = []
    for i in range(11, -1, -1):
        d  = today - relativedelta(months=i)
        r2 = sum(float(l.montant_paye) for l in loyqs.filter(echeance__month=d.month, echeance__year=d.year))
        c2 = sum(float(c.montant_ttc) for c in chqs.filter(date_charge__month=d.month, date_charge__year=d.year))
        evo.append({'mois': d.strftime('%b %Y'), 'revenus': r2, 'charges': c2})

    rappels = [
        {'type': 'retard', 'message': f'{l.locataire_nom} — {l.libelle}', 'detail': f'Solde: {float(l.solde_restant):,.0f} BIF'}
        for l in loyqs.filter(statut='retard')[:5]
    ]

    taux_comm = 0.09
    if is_proprio:
        try:
            from apps.contrats_societe.models import ContratSociete
            cs = ContratSociete.objects.filter(
                proprietaire=user.proprietaire_profile, statut='actif'
            ).first()
            if cs:
                taux_comm = float(cs.taux_commission) / 100
        except Exception:
            pass

    net_reverse = round(rev * (1 - taux_comm), 2)

    return Response({
        'locaux': {
            'total': total, 'occupes': occ, 'libres': total - occ,
            'taux_occupation': round(occ / total * 100, 1) if total else 0
        },
        'finances': {
            'revenus_mois': rev, 'charges_mois': ch,
            'benefice_net': rev - ch,
            'commission_cabinet': round(rev * taux_comm, 2),
            'net_reverse': net_reverse,
        },
        'loyers_mois': {
            'total': lm.count(), 'payes': payes,
            'retard': retard, 'taux_paiement': taux
        },
        'evolution_12_mois': evo,
        'rappels': rappels,
        '_debug': {
            'user': user.username,
            'role': user.role,
            'proprietaire_profile': str(user.proprietaire_profile) if user.proprietaire_profile else None,
            'is_proprio': is_proprio,
            'nb_locaux_filtres': total,
        }
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def portefeuille_view(request):
    from apps.locaux.models import Local
    from apps.loyers.models import Loyer
    from apps.proprietaires.models import Proprietaire
    today = timezone.now().date(); m, y = today.month, today.year
    props = Proprietaire.objects.all()
    stats = []
    for p in props:
        loyers = Loyer.objects.filter(local__proprietaire=p, echeance__month=m, echeance__year=y)
        rev = sum(float(l.montant_paye) for l in loyers); comm = round(rev*0.09,2)
        stats.append({'nom':p.nom,'nb_locaux':Local.objects.filter(proprietaire=p).count(),'revenu_brut':rev,'commission_9pct':comm,'net_verse':round(rev*0.91,2)})
    retards = Loyer.objects.filter(statut='retard')
    creances = [{'locataire':l.locataire_nom,'local':l.local_reference,'solde':float(l.solde_restant),'statut':l.statut} for l in retards]
    tot_rev = sum(float(l.montant_paye) for l in Loyer.objects.filter(echeance__month=m,echeance__year=y))
    return Response({
        'commission_cabinet_9pct': round(tot_rev*0.09,2),
        'revenus_bruts_mois': tot_rev,
        'nb_proprietaires': props.count(),
        'loyers_anticipes': 0,
        'total_creances': sum(c['solde'] for c in creances),
        'stats_par_proprietaire': stats,
        'creances_detail': creances
    })