from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import GroupChat, GroupMessage
from .serializers import GroupChatSerializer, GroupMessageSerializer


# ─────────────────────────────────────────────
#  Liste / création
# ─────────────────────────────────────────────
class GroupChatListCreate(generics.ListCreateAPIView):
    serializer_class = GroupChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = GroupChat.objects.select_related('immeuble', 'proprietaire')

        # Filtres optionnels passés en query param
        prop_id = self.request.query_params.get('proprietaire')
        imm_id  = self.request.query_params.get('immeuble')
        if prop_id:
            qs = qs.filter(proprietaire_id=prop_id)
        if imm_id:
            qs = qs.filter(immeuble_id=imm_id)

        # Restrictions par rôle
        if user.role == 'proprietaire' and user.proprietaire_profile:
            qs = qs.filter(proprietaire=user.proprietaire_profile)
        elif user.role == 'locataire' and user.locataire_profile:
            from apps.contrats.models import Contrat
            contrat = Contrat.objects.filter(
                locataire=user.locataire_profile, statut='actif'
            ).first()
            if contrat and contrat.local.immeuble:
                qs = qs.filter(immeuble=contrat.local.immeuble)
            else:
                return GroupChat.objects.none()

        return qs

    def perform_create(self, serializer):
        from rest_framework.exceptions import ValidationError
        from apps.immeubles.models import Immeuble
        from apps.proprietaires.models import Proprietaire

        immeuble_id    = self.request.data.get('immeuble')
        proprietaire_id = self.request.data.get('proprietaire')

        # ── Résoudre l'immeuble ───────────────────────────────────
        if not immeuble_id:
            raise ValidationError({'immeuble': 'Ce champ est obligatoire.'})
        try:
            immeuble = Immeuble.objects.get(pk=immeuble_id)
        except Immeuble.DoesNotExist:
            raise ValidationError({'immeuble': f'Immeuble {immeuble_id} introuvable.'})

        # ── Résoudre le propriétaire ──────────────────────────────
        # Priorité : valeur explicite → premier propriétaire de l'immeuble → erreur
        proprietaire = None
        if proprietaire_id:
            try:
                proprietaire = Proprietaire.objects.get(pk=proprietaire_id)
            except Proprietaire.DoesNotExist:
                raise ValidationError({'proprietaire': f'Propriétaire {proprietaire_id} introuvable.'})
        else:
            # Déduire depuis les locaux de l'immeuble
            from apps.locaux.models import Local
            local = Local.objects.filter(immeuble=immeuble).select_related('proprietaire').first()
            if local:
                proprietaire = local.proprietaire
            else:
                raise ValidationError({'proprietaire': 'Ce champ est obligatoire (aucun local trouvé dans cet immeuble).'})

        # ── Éviter les doublons ───────────────────────────────────
        if GroupChat.objects.filter(immeuble=immeuble).exists():
            raise ValidationError({'immeuble': 'Un groupe de chat existe déjà pour cet immeuble.'})

        # ── Créer ─────────────────────────────────────────────────
        nom = f"Chat — {immeuble.nom}"
        serializer.save(nom=nom, immeuble=immeuble, proprietaire=proprietaire)


# ─────────────────────────────────────────────
#  Détail
# ─────────────────────────────────────────────
class GroupChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    permission_classes = [IsAuthenticated]


# ─────────────────────────────────────────────
#  Messages — GET liste / POST envoi unifié
#  (prop & locataire envoient via POST /messages/)
# ─────────────────────────────────────────────
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def group_messages_or_send(request, pk):
    try:
        group = GroupChat.objects.get(pk=pk)
    except GroupChat.DoesNotExist:
        return Response({'error': 'Groupe introuvable.'}, status=404)

    if request.method == 'GET':
        msgs = group.messages.select_related('auteur').order_by('created_at')
        return Response(GroupMessageSerializer(msgs, many=True).data)

    # POST → envoyer un message
    contenu = (request.data.get('contenu') or '').strip()
    if not contenu:
        return Response({'error': 'Message vide.'}, status=400)
    msg = GroupMessage.objects.create(
        group=group,
        auteur=request.user,
        contenu=contenu,
    )
    return Response(GroupMessageSerializer(msg).data, status=201)


# ─────────────────────────────────────────────
#  Envoi explicite — POST /send/   (dashboard admin)
# ─────────────────────────────────────────────
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request, pk):
    try:
        group = GroupChat.objects.get(pk=pk)
    except GroupChat.DoesNotExist:
        return Response({'error': 'Groupe introuvable.'}, status=404)

    contenu = (request.data.get('contenu') or '').strip()
    if not contenu:
        return Response({'error': 'Message vide.'}, status=400)

    msg = GroupMessage.objects.create(
        group=group,
        auteur=request.user,
        contenu=contenu,
    )
    return Response(GroupMessageSerializer(msg).data, status=201)


# ─────────────────────────────────────────────
#  Lecture des messages — GET /messages/  (lecture seule)
#  Gardé pour compatibilité si quelqu'un l'appelle en GET seul
# ─────────────────────────────────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def group_messages(request, pk):
    try:
        group = GroupChat.objects.get(pk=pk)
    except GroupChat.DoesNotExist:
        return Response({'error': 'Groupe introuvable.'}, status=404)
    msgs = group.messages.select_related('auteur').order_by('created_at')
    return Response(GroupMessageSerializer(msgs, many=True).data)


# ─────────────────────────────────────────────
#  Hiérarchie  propriétaire → immeubles → groupes
#  appelé par le dashboard admin : /api/chat/hierarchy/?proprietaire=1
# ─────────────────────────────────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hierarchy(request):
    from apps.proprietaires.models import Proprietaire
    from apps.immeubles.models import Immeuble

    prop_id = request.query_params.get('proprietaire')
    props = Proprietaire.objects.filter(pk=prop_id) if prop_id else Proprietaire.objects.all()

    data = []
    for p in props:
        immeubles = Immeuble.objects.filter(locaux__proprietaire=p).distinct()
        imm_data = []
        for imm in immeubles:
            group = GroupChat.objects.filter(immeuble=imm).first()
            imm_data.append({
                'id':         imm.id,
                'nom':        imm.nom,
                'group_id':   group.id   if group else None,
                'group_nom':  group.nom  if group else None,
            })
        data.append({
            'id':        p.id,
            'nom':       p.nom,
            'immeubles': imm_data,
        })

    return Response(data)
