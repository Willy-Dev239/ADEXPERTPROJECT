from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Contrat, ContratSociete
from .serializers import ContratSerializer, ContratSocieteSerializer

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
