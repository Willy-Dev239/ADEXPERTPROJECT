from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'locataire' and user.locataire_profile:
            return Notification.objects.filter(destinataire_locataire=user.locataire_profile)
        return Notification.objects.all()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def marquer_lu(request, pk):
    try:
        n = Notification.objects.get(pk=pk)
        n.lu = True
        n.save()
        return Response({'ok': True})
    except Notification.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def envoyer_avertissement(request):
    """Feature 8: Admin sends warning to locataire(s)"""
    from apps.locataires.models import Locataire
    locataire_id = request.data.get('locataire_id')
    tous = request.data.get('tous', False)
    titre = request.data.get('titre', 'Avertissement')
    message = request.data.get('message', '')
    if not message:
        return Response({'error': 'Message requis.'}, status=400)
    created = 0
    if tous:
        for loc in Locataire.objects.all():
            Notification.objects.create(
                destinataire_locataire=loc, titre=titre,
                message=message, type_notif='avertissement'
            )
            created += 1
    elif locataire_id:
        try:
            loc = Locataire.objects.get(pk=locataire_id)
            Notification.objects.create(
                destinataire_locataire=loc, titre=titre,
                message=message, type_notif='avertissement'
            )
            created = 1
        except Locataire.DoesNotExist:
            return Response({'error': 'Locataire introuvable.'}, status=404)
    return Response({'detail': f'{created} notification(s) envoyée(s).'})
