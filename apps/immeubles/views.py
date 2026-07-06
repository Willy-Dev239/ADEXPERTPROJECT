from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Immeuble, PROVINCES_COMMUNES
from .serializers import ImmeubleSerializer
from .permissions import IsAdminOrGestionnaire


class ImmeubleViewSet(viewsets.ModelViewSet):
    serializer_class = ImmeubleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['proprietaire']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Immeuble.objects.all()

        if user.role == 'proprietaire' and user.proprietaire_profile:
            qs = qs.filter(locaux__proprietaire=user.proprietaire_profile).distinct()

        return qs

class ImmeubleActeursView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrGestionnaire]
    ...


class ImmeubleListCreate(generics.ListCreateAPIView):
    serializer_class = ImmeubleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'proprietaire' and user.proprietaire_profile:
            return Immeuble.objects.filter(
                locaux__proprietaire=user.proprietaire_profile
            ).distinct()
        return Immeuble.objects.all()


class ImmeubleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Immeuble.objects.all()
    serializer_class = ImmeubleSerializer
    permission_classes = [IsAuthenticated]

# views.py
from django.http import JsonResponse
from .models import Immeuble
from apps.locaux.models import Local
@permission_classes([IsAuthenticated])
def get_immeubles_by_proprietaire(request):
    proprietaire_id = request.GET.get('proprietaire_id')
    if proprietaire_id:
        # Relation indirecte : Immeuble → Local → Proprietaire
        immeuble_ids = Local.objects.filter(
            proprietaire_id=proprietaire_id
        ).values_list('immeuble_id', flat=True).distinct()
        
        immeubles = Immeuble.objects.filter(id__in=immeuble_ids)
    else:
        immeubles = Immeuble.objects.all()
    
    data = [{'id': i.id, 'nom': i.nom} for i in immeubles]
    return JsonResponse({'immeubles': data})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def provinces_communes_view(request):
    return Response(PROVINCES_COMMUNES)