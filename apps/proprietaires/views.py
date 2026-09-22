# apps/proprietaires/views.py
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.immeubles.geo import PAYS, CONTINENTS

from .models import Proprietaire
from .serializers import ProprietaireSerializer

# =====================================================================
# API GÉO — Cascade Continent → Pays → Province → Commune → Quartier
# =====================================================================

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_continents(request):
    """GET /api/proprietaires/geo/continents/"""
    return Response(list(CONTINENTS.keys()))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_pays(request):
    """GET /api/proprietaires/geo/pays/?continent=Afrique"""
    continent = request.GET.get("continent")
    if continent and continent in CONTINENTS:
        return Response(list(CONTINENTS[continent].keys()))
    return Response(list(PAYS.keys()))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_provinces(request):
    """GET /api/proprietaires/geo/provinces/  (Burundi par défaut)"""
    pays = request.GET.get("pays", "Burundi")
    if pays not in PAYS:
        return Response([])
    return Response(list(PAYS[pays].keys()))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_communes(request):
    """GET /api/proprietaires/geo/communes/?province=Bujumbura Mairie"""
    pays = request.GET.get("pays", "Burundi")
    province = request.GET.get("province")
    if not province:
        return Response([])
    return Response(list(PAYS.get(pays, {}).get(province, {}).keys()))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_quartiers(request):
    """GET /api/proprietaires/geo/quartiers/?province=...&commune=..."""
    pays = request.GET.get("pays", "Burundi")
    province = request.GET.get("province")
    commune = request.GET.get("commune")
    if not (province and commune):
        return Response([])
    return Response(PAYS.get(pays, {}).get(province, {}).get(commune, []))
# =====================================================================
# CRUD Propriétaires
# =====================================================================

class ProprietaireListCreate(generics.ListCreateAPIView):
    serializer_class = ProprietaireSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "proprietaire" and user.proprietaire_profile:
            return Proprietaire.objects.filter(pk=user.proprietaire_profile.pk)
        return Proprietaire.objects.all()


class ProprietaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer
    permission_classes = [IsAuthenticated]