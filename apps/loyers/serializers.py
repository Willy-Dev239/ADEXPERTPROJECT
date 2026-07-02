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
        try:
            uuid = str(obj.photo).strip('/')
            return f'https://ucarecdn.com/{uuid}/'
        except Exception:
            return None

    def get_locataire_nom(self, obj):
        return obj.locataire.nom_prenom

    def get_loyer_libelle(self, obj):
        return obj.loyer.libelle if obj.loyer else None

    class Meta:
        model = Bordereau
        fields = '__all__'