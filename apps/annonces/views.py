from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_GET
from rest_framework import generics
from rest_framework.decorators import (
    api_view, parser_classes, permission_classes,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Annonce, AnnoncePhoto
from .permissions import PeutEcrire
from .serializers import AnnoncePubliqueSerializer, AnnonceSerializer


def _annonces_qs():
    """Queryset optimisé : photos SANS les octets."""
    return Annonce.objects.select_related('local').prefetch_related(
        Prefetch(
            'photos',
            queryset=AnnoncePhoto.objects.defer('donnees'),
        )
    )


def _reponse_annonce(request, pk, status=200):
    annonce = _annonces_qs().get(pk=pk)
    data = AnnonceSerializer(annonce, context={'request': request}).data
    return Response(data, status=status)


# =====================================================================
# PUBLIC (sans authentification)
# =====================================================================

class AnnoncePubliqueList(generics.ListAPIView):
    """GET /api/annonces/public/ — annonces publiées uniquement."""
    serializer_class = AnnoncePubliqueSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    pagination_class = None

    def get_queryset(self):
        return _annonces_qs().filter(statut='publiee')


@require_GET
def annonce_photo(request, pk):
    """GET /api/annonces/photos/<id>/ — sert l'image depuis la base."""
    photo = get_object_or_404(AnnoncePhoto, pk=pk)
    reponse = HttpResponse(
        bytes(photo.donnees), content_type=photo.content_type
    )
    reponse['Cache-Control'] = 'public, max-age=86400'
    return reponse


# =====================================================================
# GESTION (admin / gestionnaire)
# =====================================================================

class AnnonceListCreate(generics.ListCreateAPIView):
    serializer_class = AnnonceSerializer
    permission_classes = [PeutEcrire]

    def get_queryset(self):
        qs = _annonces_qs()
        statut = self.request.query_params.get('statut')
        if statut:
            qs = qs.filter(statut=statut)
        return qs

    def perform_create(self, serializer):
        serializer.save(publie_par=self.request.user)


class AnnonceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnnonceSerializer
    permission_classes = [PeutEcrire]

    def get_queryset(self):
        return _annonces_qs()


@api_view(['POST'])
@permission_classes([PeutEcrire])
def marquer_louee(request, pk):
    """POST /api/annonces/<id>/marquer-louee/"""
    annonce = get_object_or_404(Annonce, pk=pk)
    if annonce.statut != 'publiee':
        return Response(
            {'detail': "Seule une annonce publiée peut être marquée louée."},
            status=400,
        )
    annonce.marquer_louee()
    return _reponse_annonce(request, pk)


@api_view(['POST'])
@permission_classes([PeutEcrire])
def retirer(request, pk):
    """POST /api/annonces/<id>/retirer/"""
    annonce = get_object_or_404(Annonce, pk=pk)
    if annonce.statut != 'publiee':
        return Response(
            {'detail': "Seule une annonce publiée peut être retirée."},
            status=400,
        )
    annonce.retirer()
    return _reponse_annonce(request, pk)


@api_view(['POST'])
@permission_classes([PeutEcrire])
def republier(request, pk):
    """POST /api/annonces/<id>/republier/ — remet en ligne (local à nouveau libre)."""
    annonce = get_object_or_404(Annonce, pk=pk)
    local = annonce.local

    if annonce.statut == 'publiee':
        return Response({'detail': "Annonce déjà publiée."}, status=400)
    if local.est_occupe or local.statut != 'libre':
        return Response(
            {'detail': "Le local n'est pas libre."}, status=400
        )
    if Annonce.objects.filter(
        local=local, statut='publiee'
    ).exclude(pk=annonce.pk).exists():
        return Response(
            {'detail': "Ce local a déjà une annonce publiée."}, status=400
        )

    annonce.statut = 'publiee'
    annonce.date_retrait = None
    annonce.date_publication = timezone.now()
    annonce.save(
        update_fields=['statut', 'date_retrait', 'date_publication', 'updated_at']
    )
    return _reponse_annonce(request, pk)


@api_view(['POST'])
@permission_classes([PeutEcrire])
@parser_classes([MultiPartParser, FormParser])
def ajouter_photos(request, pk):
    """POST /api/annonces/<id>/photos/ — multipart, champ « photos » (multiple)."""
    annonce = get_object_or_404(Annonce, pk=pk)
    fichiers = request.FILES.getlist('photos')
    if not fichiers:
        return Response(
            {'detail': "Aucune photo reçue (champ « photos »)."}, status=400
        )

    try:
        with transaction.atomic():
            for fichier in fichiers:
                AnnoncePhoto.depuis_fichier(annonce, fichier)
    except DjangoValidationError as e:
        return Response({'detail': ' '.join(e.messages)}, status=400)

    return _reponse_annonce(request, pk, status=201)


@api_view(['DELETE'])
@permission_classes([PeutEcrire])
def supprimer_photo(request, pk):
    """DELETE /api/annonces/photos/<id>/supprimer/"""
    photo = get_object_or_404(AnnoncePhoto.objects.defer('donnees'), pk=pk)
    photo.delete()
    return Response(status=204)