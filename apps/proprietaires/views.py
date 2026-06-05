from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Proprietaire
from .serializers import ProprietaireSerializer

class ProprietaireListCreate(generics.ListCreateAPIView):
    serializer_class = ProprietaireSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.role == 'proprietaire' and user.proprietaire_profile:
            return Proprietaire.objects.filter(pk=user.proprietaire_profile.pk)
        return Proprietaire.objects.all()

class ProprietaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer
    permission_classes = [IsAuthenticated]
