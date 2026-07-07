from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets
from django.utils import timezone
from datetime import timedelta
from .models import Contrat, ContratSociete, BordereauVirement
from .serializers import ContratSerializer, ContratSocieteSerializer, BordereauVirementSerializer
class ContratListCreate(generics.ListCreateAPIView):
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = Contrat.objects.select_related('locataire','local')
        user = self.request.user
        if user.role == 'locataire' and user.locataire_profile:
            qs = qs.filter(locataire=user.locataire_profile)
        elif user.role == 'proprietaire' and user.proprietaire_profile:
            qs = qs.filter(local__proprietaire=user.proprietaire_profile)
        s = self.request.query_params.get('statut')
        if s: qs = qs.filter(statut=s)
        return qs

class ContratDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resilier_contrat(request, pk):
    try:
        c = Contrat.objects.get(pk=pk)
        c.statut = 'resilie'
        c.date_sortie = timezone.now().date()
        c.save()
        return Response({'detail': 'Contrat résilié.'})
    except Contrat.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generer_loyers(request, pk):
    from apps.loyers.models import Loyer
    from dateutil.relativedelta import relativedelta
    try:
        contrat = Contrat.objects.get(pk=pk)
    except Contrat.DoesNotExist:
        return Response({'error': 'Introuvable.'}, status=404)
    nb_mois = int(request.data.get('nb_mois', 12))
    date_str = request.data.get('date_debut')
    from datetime import date
    current = date.fromisoformat(date_str) if date_str else contrat.date_entree
    delta_map = {'mensuel':1,'bimensuel':2,'trimestriel':3,'semestriel':6,'annuel':12}
    delta = delta_map.get(contrat.periodicite, 1)
    created = 0
    for _ in range(nb_mois // delta):
        fin = current + relativedelta(months=delta) - timedelta(days=1)
        label = f"Loyer {current.strftime('%B %Y').capitalize()}"
        if not Loyer.objects.filter(contrat=contrat, libelle=label).exists():
            Loyer.objects.create(contrat=contrat, locataire=contrat.locataire, local=contrat.local,
                libelle=label, periode_debut=current, periode_fin=fin,
                loyer_hors_charges=contrat.loyer_hors_charges, charges=contrat.provisions_charges, echeance=current)
            created += 1
        current += relativedelta(months=delta)
    return Response({'message': f'{created} loyer(s) créé(s).', 'created': created})

class ContratSocieteListCreate(generics.ListCreateAPIView):
    serializer_class = ContratSocieteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = ContratSociete.objects.select_related('proprietaire')
        user = self.request.user
        if user.role == 'proprietaire' and user.proprietaire_profile:
            qs = qs.filter(proprietaire=user.proprietaire_profile)
        s = self.request.query_params.get('statut')
        if s: qs = qs.filter(statut=s)
        return qs

class ContratSocieteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContratSociete.objects.all()
    serializer_class = ContratSocieteSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class BordereauVirementViewSet(viewsets.ModelViewSet):
    serializer_class = BordereauVirementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = BordereauVirement.objects.select_related('proprietaire', 'contrat_societe')
        if user.role == 'proprietaire':
            return qs.filter(proprietaire=user.proprietaire_profile)
        elif user.role in ('admin', 'gestionnaire'):
            statut = self.request.query_params.get('statut')
            if statut:
                qs = qs.filter(statut=statut)
            return qs
        return qs.none()

    def perform_create(self, serializer):
        if self.request.user.role != 'proprietaire':
            raise PermissionDenied("Seul un propriétaire peut envoyer un bordereau de virement.")
        serializer.save()

    @action(detail=True, methods=['post'], url_path='valider')
    def valider(self, request, pk=None):
        if request.user.role not in ('admin', 'gestionnaire'):
            raise PermissionDenied("Action réservée à l'administration.")
        obj = self.get_object()
        obj.statut = 'valide'
        obj.traite_par = request.user
        obj.date_traitement = timezone.now()
        obj.save()
        return Response(self.get_serializer(obj).data)

    @action(detail=True, methods=['post'], url_path='rejeter')
    def rejeter(self, request, pk=None):
        if request.user.role not in ('admin', 'gestionnaire'):
            raise PermissionDenied("Action réservée à l'administration.")
        obj = self.get_object()
        obj.statut = 'rejete'
        obj.commentaire_admin = request.data.get('commentaire', '')
        obj.traite_par = request.user
        obj.date_traitement = timezone.now()
        obj.save()
        return Response(self.get_serializer(obj).data)
