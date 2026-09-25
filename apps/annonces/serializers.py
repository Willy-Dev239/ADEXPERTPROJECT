from django.urls import reverse
from rest_framework import serializers

from .models import Annonce


def _photos_annonce(annonce):
    """Liste {id, url} des photos, sans charger les octets."""
    cache = getattr(annonce, '_prefetched_objects_cache', {})
    if 'photos' in cache:
        photos = annonce.photos.all()
    else:
        photos = annonce.photos.defer('donnees')
    return [
        {'id': p.id, 'url': reverse('annonce_photo', args=[p.id])}
        for p in photos
    ]


class AnnonceSerializer(serializers.ModelSerializer):
    """Serializer de gestion (admin / gestionnaire)."""

    local_reference = serializers.CharField(
        source='local.reference', read_only=True
    )
    type_local = serializers.CharField(
        source='local.type_local_display', read_only=True
    )
    localisation = serializers.CharField(read_only=True)
    statut_display = serializers.CharField(
        source='get_statut_display', read_only=True
    )
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Annonce
        fields = [
            'id', 'local', 'local_reference', 'type_local', 'localisation',
            'titre', 'description', 'loyer',
            'contact_telephone', 'contact_whatsapp',
            'statut', 'statut_display',
            'date_publication', 'date_retrait',
            'publie_par', 'created_at', 'updated_at',
            'photos',
        ]
        read_only_fields = [
            'statut', 'date_publication', 'date_retrait',
            'publie_par', 'created_at', 'updated_at',
        ]

    def get_photos(self, obj):
        return _photos_annonce(obj)

    def validate_loyer(self, valeur):
        if valeur <= 0:
            raise serializers.ValidationError("Le loyer doit être positif.")
        return valeur

    def validate_local(self, local):
        if self.instance is not None:
            if local != self.instance.local:
                raise serializers.ValidationError(
                    "Le local d'une annonce ne peut pas être modifié."
                )
            return local

        if local.est_occupe or local.statut != 'libre':
            raise serializers.ValidationError(
                "Seuls les locaux libres peuvent être publiés."
            )
        if Annonce.objects.filter(local=local, statut='publiee').exists():
            raise serializers.ValidationError(
                "Ce local a déjà une annonce publiée."
            )
        return local


class AnnoncePubliqueSerializer(serializers.ModelSerializer):
    """Serializer public : aucune donnée interne (référence, propriétaire...)."""

    type_local = serializers.CharField(
        source='local.type_local_display', read_only=True
    )
    localisation = serializers.CharField(read_only=True)
    superficie = serializers.DecimalField(
        source='local.superficie', max_digits=8, decimal_places=2,
        read_only=True,
    )
    meuble = serializers.BooleanField(source='local.meuble', read_only=True)
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Annonce
        fields = [
            'id', 'titre', 'description', 'loyer',
            'type_local', 'localisation', 'superficie', 'meuble',
            'contact_telephone', 'contact_whatsapp',
            'date_publication', 'photos',
        ]

    def get_photos(self, obj):
        return _photos_annonce(obj)