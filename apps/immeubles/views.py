from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Immeuble, PROVINCES_COMMUNES
from .serializers import ImmeubleSerializer
# views.py  (ajouter)
from .permissions import IsAdminOrGestionnaire
from rest_framework.views import APIView

class ImmeubleActeursView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrGestionnaire]
    ...
class ImmeubleListCreate(generics.ListCreateAPIView):
    serializer_class = ImmeubleSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.role == 'proprietaire' and user.proprietaire_profile:
            return Immeuble.objects.filter(locaux__proprietaire=user.proprietaire_profile).distinct()
        return Immeuble.objects.all()

class ImmeubleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Immeuble.objects.all()
    serializer_class = ImmeubleSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def provinces_communes_view(request):
    return Response(PROVINCES_COMMUNES)
