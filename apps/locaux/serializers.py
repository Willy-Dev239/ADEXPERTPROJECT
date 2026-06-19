from rest_framework import serializers
from .models import Local
class LocalSerializer(serializers.ModelSerializer):
    est_occupe = serializers.ReadOnlyField()
    proprietaire_nom = serializers.ReadOnlyField()
    type_local_display = serializers.ReadOnlyField()
    adresse_complete = serializers.ReadOnlyField()
    
    class Meta:
        model = Local
        fields = '__all__'
from rest_framework import serializers
from .models import Local

class LocalSerializer(serializers.ModelSerializer):
    est_occupe = serializers.ReadOnlyField()
    proprietaire_nom = serializers.ReadOnlyField()
    type_local_display = serializers.ReadOnlyField()
    adresse_complete = serializers.ReadOnlyField()
    

    

    class Meta:
        model = Local
        fields = '__all__'