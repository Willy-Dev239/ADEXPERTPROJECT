# apps/locaux/views.py
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.immeubles.geo import PAYS, CONTINENTS

from .models import Local
from .serializers import LocalSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_provinces(request):
    """GET /api/locaux/geo/provinces/  (Burundi par défaut)"""
    pays = request.GET.get("pays", "Burundi")
    if pays not in PAYS:
        return Response([])
    return Response(list(PAYS[pays].keys()))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_communes(request):
    """GET /api/locaux/geo/communes/?province=Bujumbura Mairie"""
    pays = request.GET.get("pays", "Burundi")
    province = request.GET.get("province")
    if not province:
        return Response([])
    return Response(list(PAYS.get(pays, {}).get(province, {}).keys()))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_quartiers(request):
    """GET /api/locaux/geo/quartiers/?province=...&commune=..."""
    pays = request.GET.get("pays", "Burundi")
    province = request.GET.get("province")
    commune = request.GET.get("commune")
    if not (province and commune):
        return Response([])
    return Response(PAYS.get(pays, {}).get(province, {}).get(commune, []))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_continents(request):
    """GET /api/locaux/geo/continents/"""
    return Response(list(CONTINENTS.keys()))
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def geo_pays(request):
    """GET /api/locaux/geo/pays/?continent=Afrique"""
    continent = request.GET.get("continent")
    if continent and continent in CONTINENTS:
        return Response(list(CONTINENTS[continent].keys()))
    return Response(list(PAYS.keys()))
# =====================================================================
# CRUD Locaux — ta logique conservée à l'identique
# =====================================================================

class LocalListCreate(generics.ListCreateAPIView):
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Local.objects.select_related("proprietaire", "immeuble")

        if user.role == "proprietaire" and user.proprietaire_profile:
            return qs.filter(proprietaire=user.proprietaire_profile)

        t = self.request.query_params.get("type_local")
        if t:
            qs = qs.filter(type_local=t)

        return qs


class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]