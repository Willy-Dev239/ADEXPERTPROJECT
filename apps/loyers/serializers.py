from rest_framework import serializers
from .models import Loyer, Paiement, Bordereau


class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']


class LoyerSerializer(serializers.ModelSerializer):
    locataire_nom = serializers.ReadOnlyField()
    local_reference = serializers.ReadOnlyField()
    montant_total = serializers.ReadOnlyField()
    montant_paye = serializers.ReadOnlyField()
    solde_restant = serializers.ReadOnlyField()
    statut_display = serializers.SerializerMethodField()
    paiements = PaiementSerializer(many=True, read_only=True)

    def get_statut_display(self, obj):
        return obj.get_statut_display_custom()

    class Meta:
        model = Loyer
        fields = '__all__'


class BordereauSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    locataire_nom = serializers.SerializerMethodField()
    loyer_libelle = serializers.SerializerMethodField()

    def get_photo_url(self, obj):
        if not obj.photo:
            return None
        request = self.context.get('request')
        url = obj.photo.url
        return request.build_absolute_uri(url) if request else url

    def get_locataire_nom(self, obj):
        return obj.locataire.nom_prenom

    def get_loyer_libelle(self, obj):
        return obj.loyer.libelle if obj.loyer else None

    class Meta:
        model = Bordereau
        fields = '__all__'
        read_only_fields = ['numero', 'created_at', 'statut', 'commentaire_admin']


class BordereauCreateSerializer(serializers.ModelSerializer):
    """
    Serializer dédié à la création d'un bordereau par le locataire
    (upload multipart : photo directement stockée dans media/bordereaux/<annee>/<mois>/).
    """
    loyer_id = serializers.PrimaryKeyRelatedField(
        queryset=Loyer.objects.all(), source='loyer', write_only=True
    )

    class Meta:
        model = Bordereau
        fields = ['loyer_id', 'montant', 'date_paiement', 'banque', 'reference_client', 'photo', 'notes']

    def validate_reference_client(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("La référence est obligatoire.")
        if Bordereau.objects.filter(reference_client__iexact=value).exists():
            raise serializers.ValidationError(
                "Cette référence existe déjà. Veuillez saisir une référence différente."
            )
        return value

    def validate_banque(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("La banque est obligatoire.")
        return value