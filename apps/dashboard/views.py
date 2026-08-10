from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    from apps.locaux.models import Local
    from apps.loyers.models import Loyer, Paiement
    from apps.charges.models import Charge
    from apps.contrats.models import ContratSociete
    from dateutil.relativedelta import relativedelta

    user = request.user
    today = timezone.now().date()
    m, y = today.month, today.year

    lqs   = Local.objects.all()
    loyqs = Loyer.objects.all()
    chqs  = Charge.objects.all()

    # ─── Filtre propriétaire ─────────────────────────────────────────────────
    is_proprio = (user.role == 'proprietaire' and user.proprietaire_profile is not None)
    filtre_proprio_id = None
    if is_proprio:
        p = user.proprietaire_profile
        filtre_proprio_id = p.id
        lqs   = lqs.filter(proprietaire=p)
        loyqs = loyqs.filter(local__proprietaire=p)
        chqs  = chqs.filter(local__proprietaire=p)
    else:
        # Admin/Gestionnaire : filtre optionnel via query param
        prop_id = request.GET.get('proprietaire')
        if prop_id:
            filtre_proprio_id = prop_id
            lqs   = lqs.filter(proprietaire_id=prop_id)
            loyqs = loyqs.filter(local__proprietaire_id=prop_id)
            chqs  = chqs.filter(local__proprietaire_id=prop_id)

    # ─── Filtre immeuble ──────────────────────────────────────────────────────
    immeuble_id = request.GET.get('immeuble')
    if immeuble_id:
        lqs   = lqs.filter(immeuble_id=immeuble_id)
        loyqs = loyqs.filter(local__immeuble_id=immeuble_id)
        chqs  = chqs.filter(immeuble_id=immeuble_id)

    total  = lqs.count()
    occ    = sum(1 for l in lqs if l.est_occupe)
    lm     = loyqs.filter(echeance__month=m, echeance__year=y)

    # ✅ Revenus du mois : basés sur la date réelle d'encaissement, paiements actifs uniquement
    rev = sum(float(p.montant) for p in Paiement.objects.filter(
        date_paiement__month=m, date_paiement__year=y, loyer__local__in=lqs, annule=False
    ))

    # ─── Revenu annuel : basé sur la date réelle d'encaissement, pas l'échéance ──
    rev_annuel = sum(float(p.montant) for p in Paiement.objects.filter(
        date_paiement__year=y, loyer__local__in=lqs, annule=False
    ))

    ch     = sum(float(c.montant_ttc) for c in chqs.filter(date_charge__month=m, date_charge__year=y))
    payes  = lm.filter(statut='paye').count()
    retard = lm.filter(statut='retard').count()
    taux   = round(payes / lm.count() * 100, 1) if lm.count() else 0

    evo = []
    for i in range(11, -1, -1):
        d  = today - relativedelta(months=i)
        r2 = sum(float(p.montant) for p in Paiement.objects.filter(
            date_paiement__month=d.month, date_paiement__year=d.year, loyer__local__in=lqs, annule=False
        ))
        c2 = sum(float(c.montant_ttc) for c in chqs.filter(date_charge__month=d.month, date_charge__year=d.year))
        evo.append({'mois': d.strftime('%b %Y'), 'revenus': r2, 'charges': c2})

    rappels = [
        {'type': 'retard', 'message': f'{l.locataire_nom} — {l.libelle}', 'detail': f'Solde: {float(l.solde_restant):,.0f} BIF'}
        for l in loyqs.filter(statut='retard')[:5]
    ]

    # ─── Commission cabinet : taux réel par propriétaire (ContratSociete actif) ──
    DEFAULT_TAUX = 0.09  # fallback si aucun contrat actif trouvé

    if filtre_proprio_id:
        # Un seul propriétaire concerné (proprio connecté ou filtre admin)
        taux_comm = DEFAULT_TAUX
        cs = ContratSociete.objects.filter(
            proprietaire_id=filtre_proprio_id, statut='actif'
        ).first()
        if cs:
            taux_comm = float(cs.taux_commission) / 100
        commission_cabinet = round(rev * taux_comm, 2)
    else:
        # Vue admin globale : plusieurs propriétaires, taux potentiellement différents
        taux_par_proprio = {
            cs.proprietaire_id: float(cs.taux_commission) / 100
            for cs in ContratSociete.objects.filter(statut='actif')
        }
        commission_cabinet = 0.0
        for p in Paiement.objects.filter(
            date_paiement__month=m, date_paiement__year=y, loyer__local__in=lqs, annule=False
        ).select_related('loyer__local__proprietaire'):
            t = taux_par_proprio.get(p.loyer.local.proprietaire_id, DEFAULT_TAUX)
            commission_cabinet += float(p.montant) * t
        commission_cabinet = round(commission_cabinet, 2)
        # taux moyen pondéré, uniquement pour affichage éventuel
        taux_comm = round(commission_cabinet / rev, 4) if rev else DEFAULT_TAUX

    net_reverse = round(rev - commission_cabinet, 2)

    return Response({
        'locaux': {
            'total': total, 'occupes': occ, 'libres': total - occ,
            'taux_occupation': round(occ / total * 100, 1) if total else 0
        },
       'finances': {
            'revenus_mois': rev, 'charges_mois': ch,
            'revenus_annee': rev_annuel,
            'benefice_net': rev - ch,
            'commission_cabinet': commission_cabinet,
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
            'filtre_proprietaire': request.GET.get('proprietaire'),
            'filtre_immeuble': request.GET.get('immeuble'),
        }
    })
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def portefeuille_view(request):
    import traceback
    try:
        from apps.locaux.models import Local
        from apps.loyers.models import Loyer, Paiement
        from apps.proprietaires.models import Proprietaire
        from apps.contrats.models import ContratSociete
        today = timezone.now().date(); m, y = today.month, today.year
        props = Proprietaire.objects.all()
        stats = []
        tot_comm_cabinet = 0

        for p in props:
            rev = sum(float(pm.montant) for pm in Paiement.objects.filter(
                date_paiement__month=m, date_paiement__year=y,
                loyer__local__proprietaire=p, annule=False
            ))

            taux_comm = 0.09
            cs = ContratSociete.objects.filter(proprietaire=p, statut='actif').first()
            if cs:
                taux_comm = float(cs.taux_commission) / 100

            comm = round(rev * taux_comm, 2)
            tot_comm_cabinet += comm

            stats.append({
                'nom': p.nom,
                'nb_locaux': Local.objects.filter(proprietaire=p).count(),
                'revenu_brut': rev,
                'commission_9pct': comm,
                'taux_commission': round(taux_comm * 100, 2),
                'net_verse': round(rev * (1 - taux_comm), 2)
            })

        retards = Loyer.objects.filter(statut='retard')
        creances = [{'locataire':l.locataire_nom,'local':l.local_reference,'solde':float(l.solde_restant),'statut':l.statut} for l in retards]
        tot_rev = sum(float(pm.montant) for pm in Paiement.objects.filter(
            date_paiement__month=m, date_paiement__year=y, annule=False
        ))

        return Response({
            'commission_cabinet_9pct': round(tot_comm_cabinet, 2),
            'revenus_bruts_mois': tot_rev,
            'nb_proprietaires': props.count(),
            'loyers_anticipes': 0,
            'total_creances': sum(c['solde'] for c in creances),
            'stats_par_proprietaire': stats,
            'creances_detail': creances
        })
    except Exception as e:
        return Response({'error': str(e), 'traceback': traceback.format_exc()}, status=500)