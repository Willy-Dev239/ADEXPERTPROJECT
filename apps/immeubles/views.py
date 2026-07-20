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

    def get(self, request, immeuble_id):
        try:
            immeuble = Immeuble.objects.get(pk=immeuble_id)
        except Immeuble.DoesNotExist:
            return Response({'detail': 'Immeuble introuvable.'}, status=404)

        locaux = Local.objects.filter(immeuble=immeuble)
        acteurs = []

        # ── PROPRIÉTAIRES ──
        from apps.proprietaires.models import Proprietaire
        proprietaires = Proprietaire.objects.filter(locaux__in=locaux).distinct()
        for p in proprietaires:
            ua = getattr(p, 'user_account', None)
            local_ref = locaux.filter(proprietaire=p).values_list('reference', flat=True).first()
            acteurs.append({
                'id': ua.id if ua else None,
                'nom_prenom': p.nom,
                'username': ua.username if ua else '',
                'email': (ua.email if ua else p.email) or '',
                'telephone': p.telephone,
                'role': 'proprietaire',
                'is_active': ua.is_active if ua else True,
                'last_login': ua.last_login if ua else None,
                'date_joined': ua.date_joined if ua else None,
                'mot_de_passe_temp': p.mot_de_passe_temp,
                'local_reference': local_ref or '',
                'immeuble_nom': immeuble.nom,
            })

        # ── LOCATAIRES ──
        from apps.locataires.models import Locataire
        locataires = Locataire.objects.filter(contrats__local__in=locaux, contrats__statut='actif').distinct()
        for loc in locataires:
            ua = getattr(loc, 'user_account', None)
            local_actuel = loc.local_actuel
            acteurs.append({
                'id': ua.id if ua else None,
                'nom_prenom': loc.nom_prenom,
                'username': ua.username if ua else '',
                'email': (ua.email if ua else loc.email) or '',
                'telephone': loc.telephone,
                'role': 'locataire',
                'is_active': ua.is_active if ua else True,
                'last_login': ua.last_login if ua else None,
                'date_joined': ua.date_joined if ua else None,
                'mot_de_passe_temp': loc.mot_de_passe_temp,
                'local_reference': local_actuel.reference if local_actuel else '',
                'immeuble_nom': immeuble.nom,
            })

        # ── GESTIONNAIRES & ADMINS (globaux à la plateforme) ──
        from apps.auth_app.models import User
        staff = User.objects.filter(role__in=['gestionnaire', 'admin'])
        for u in staff:
            acteurs.append({
                'id': u.id,
                'nom_prenom': u.full_name,
                'username': u.username,
                'email': u.email or '',
                'telephone': u.telephone,
                'role': u.role,
                'is_active': u.is_active,
                'last_login': u.last_login,
                'date_joined': u.date_joined,
                'mot_de_passe_temp': '',
                'local_reference': '',
                'immeuble_nom': immeuble.nom,
            })

        return Response({'acteurs': acteurs})
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