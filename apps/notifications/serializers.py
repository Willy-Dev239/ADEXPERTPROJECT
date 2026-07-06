from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    destinataire_locataire_nom = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = '__all__'

    def get_destinataire_locataire_nom(self, obj):
        return obj.destinataire_locataire.nom_prenom if obj.destinataire_locataire else None