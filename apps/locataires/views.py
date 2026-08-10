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
