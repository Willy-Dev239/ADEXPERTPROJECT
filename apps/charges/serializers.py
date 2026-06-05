from rest_framework import serializers
from .models import Charge
class ChargeSerializer(serializers.ModelSerializer):
    local_reference = serializers.ReadOnlyField()
    immeuble_nom = serializers.ReadOnlyField()
    type_display = serializers.ReadOnlyField()
    class Meta:
        model = Charge
        fields = '__all__'
