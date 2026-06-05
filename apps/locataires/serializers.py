from rest_framework import serializers
from .models import Locataire
from apps.locaux.serializers import LocalSerializer
class LocataireSerializer(serializers.ModelSerializer):
    local_actuel = LocalSerializer(read_only=True)
    situation_financiere = serializers.ReadOnlyField()
    class Meta:
        model = Locataire
        fields = '__all__'
