from rest_framework import serializers
from .models import Immeuble
class ImmeubleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immeuble
        fields = '__all__'
