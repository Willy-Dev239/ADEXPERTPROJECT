from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Immeuble, PROVINCES_COMMUNES
from .serializers import ImmeubleSerializer
from .permissions import IsAdminOrGestionnaire


class ImmeubleViewSet(viewsets.ModelViewSet):
    queryset = Immeuble.objects.all()
    serializer_class = ImmeubleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['proprietaire']  # active ?proprietaire=<id>


class ImmeubleActeursView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrGestionnaire]
    ...


class ImmeubleListCreate(generics.ListCreateAPIView):
    serializer_class = ImmeubleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'proprietaire' and user.proprietaire_profile:
            return Immeuble.objects.filter(
                locaux__proprietaire=user.proprietaire_profile
            ).distinct()
        return Immeuble.objects.all()


class ImmeubleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Immeuble.objects.all()
    serializer_class = ImmeubleSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def provinces_communes_view(request):
    return Response(PROVINCES_COMMUNES)