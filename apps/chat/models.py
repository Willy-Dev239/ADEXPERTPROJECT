from django.db import models

class GroupChat(models.Model):
    immeuble = models.OneToOneField('immeubles.Immeuble', on_delete=models.CASCADE, related_name='group_chat')
    proprietaire = models.ForeignKey('proprietaires.Proprietaire', on_delete=models.CASCADE, related_name='group_chats')
    nom = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['immeuble__nom']
    def __str__(self):
        return f"Chat — {self.immeuble.nom}"

class GroupMessage(models.Model):
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name='messages')
    auteur = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True)
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def auteur_nom(self):
        return self.auteur.full_name if self.auteur else 'Système'
    @property
    def auteur_role(self):
        return self.auteur.role if self.auteur else ''
    class Meta:
        ordering = ['created_at']
