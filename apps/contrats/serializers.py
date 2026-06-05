from rest_framework import serializers
from .models import Contrat, ContratSociete
class ContratSerializer(serializers.ModelSerializer):
    locataire_nom = serializers.ReadOnlyField()
    local_reference = serializers.ReadOnlyField()
    statut_display = serializers.ReadOnlyField()
    periodicite_display = serializers.ReadOnlyField()
    class Meta:
        model = Contrat
        fields = '__all__'
class ContratSocieteSerializer(serializers.ModelSerializer):
    proprietaire_nom = serializers.ReadOnlyField()
    statut_display = serializers.ReadOnlyField()
    class Meta:
        model = ContratSociete
        fields = '__all__'
