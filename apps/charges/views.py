from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import Charge
from .serializers import ChargeSerializer

class ChargeListCreate(generics.ListCreateAPIView):
    serializer_class = ChargeSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = Charge.objects.select_related('local','immeuble')
        t = self.request.query_params.get('type_charge')
        user = self.request.user
         # ✅ Filtre par propriétaire
        if user.role == 'proprietaire' and user.proprietaire_profile:
            qs = qs.filter(local__proprietaire=user.proprietaire_profile)
        t = self.request.query_params.get('type_charge')
        if t: qs = qs.filter(type_charge=t)
        return qs

class ChargeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rapport_mensuel_charges(request):
    mois = int(request.query_params.get('mois', timezone.now().month))
    annee = int(request.query_params.get('annee', timezone.now().year))
    qs = Charge.objects.filter(date_charge__month=mois, date_charge__year=annee)
  
    user = request.user
    if user.role == 'proprietaire' and user.proprietaire_profile:
        qs = qs.filter(local__proprietaire=user.proprietaire_profile)
    total = sum(float(c.montant_ttc) for c in qs)
    rep = {}
    for c in qs:
        rep[c.type_display] = rep.get(c.type_display, 0) + float(c.montant_ttc)
    return Response({
        'nombre_charges': qs.count(),
        'total_charges': total,
        'repartition_par_type': rep
    })
    

