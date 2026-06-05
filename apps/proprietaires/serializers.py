from rest_framework import serializers
from .models import Proprietaire
class ProprietaireSerializer(serializers.ModelSerializer):
    nb_locaux = serializers.ReadOnlyField()
    class Meta:
        model = Proprietaire
        fields = '__all__'
