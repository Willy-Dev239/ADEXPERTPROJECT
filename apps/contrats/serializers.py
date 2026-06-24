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

    def validate(self, data):
        date_entree = data.get('date_entree')
        date_sortie = data.get('date_sortie')
        if date_sortie and date_entree and date_sortie <= date_entree:
            raise serializers.ValidationError({
                'date_sortie': "La date de sortie doit être postérieure à la date d'entrée."
            })
        return data


class ContratSocieteSerializer(serializers.ModelSerializer):
    proprietaire_nom = serializers.ReadOnlyField()
    statut_display = serializers.ReadOnlyField()

    class Meta:
        model = ContratSociete
        fields = '__all__'

    def validate(self, data):
        date_signature = data.get('date_signature')
        date_effet = data.get('date_effet')
        date_expiration = data.get('date_expiration')
        if date_effet and date_signature and date_effet < date_signature:
            raise serializers.ValidationError({
                'date_effet': "La date d'effet ne peut pas être antérieure à la date de signature."
            })
        if date_expiration and date_effet and date_expiration <= date_effet:
            raise serializers.ValidationError({
                'date_expiration': "La date d'expiration doit être postérieure à la date d'effet."
            })
        return data