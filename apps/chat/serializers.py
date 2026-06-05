from rest_framework import serializers
from .models import GroupChat, GroupMessage


class GroupMessageSerializer(serializers.ModelSerializer):
    auteur_nom  = serializers.ReadOnlyField()
    auteur_role = serializers.ReadOnlyField()

    class Meta:
        model  = GroupMessage
        fields = ['id', 'group', 'auteur', 'auteur_nom', 'auteur_role', 'contenu', 'created_at']
        read_only_fields = ['auteur', 'created_at']


class GroupChatSerializer(serializers.ModelSerializer):
    immeuble_nom     = serializers.SerializerMethodField()
    proprietaire_nom = serializers.SerializerMethodField()
    nb_messages      = serializers.SerializerMethodField()
    dernier_message  = serializers.SerializerMethodField()

    # Champs gérés par perform_create → non obligatoires en écriture
    nom          = serializers.CharField(required=False, allow_blank=True, default='')
    immeuble     = serializers.IntegerField(required=False, write_only=False,
                       source='immeuble_id', allow_null=True)
    proprietaire = serializers.IntegerField(required=False, write_only=False,
                       source='proprietaire_id', allow_null=True)

    def get_immeuble_nom(self, obj):
        return obj.immeuble.nom if obj.immeuble_id else '—'

    def get_proprietaire_nom(self, obj):
        return obj.proprietaire.nom if obj.proprietaire_id else '—'

    def get_nb_messages(self, obj):
        return obj.messages.count()

    def get_dernier_message(self, obj):
        last = obj.messages.order_by('-created_at').first()
        if not last:
            return None
        return {
            'contenu': last.contenu[:80],
            'auteur':  last.auteur_nom,
            'date':    last.created_at,
        }

    class Meta:
        model  = GroupChat
        fields = [
            'id', 'nom', 'immeuble', 'proprietaire',
            'immeuble_nom', 'proprietaire_nom',
            'nb_messages', 'dernier_message', 'created_at',
        ]
