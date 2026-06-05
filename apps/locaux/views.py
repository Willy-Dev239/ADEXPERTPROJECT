from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Local
from .serializers import LocalSerializer

class LocalListCreate(generics.ListCreateAPIView):
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        qs = Local.objects.select_related('proprietaire','immeuble')
        if user.role == 'proprietaire' and user.proprietaire_profile:
            return qs.filter(proprietaire=user.proprietaire_profile)
        t = self.request.query_params.get('type_local')
        if t: qs = qs.filter(type_local=t)
        return qs

class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]
