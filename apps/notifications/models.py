from django.db import models

class Notification(models.Model):
    TYPE_CHOICES = [
        ('paiement', 'Paiement'),
        ('bordereau', 'Bordereau'),
        ('rappel', 'Rappel'),
        ('message', 'Message'),
        ('avertissement', 'Avertissement'),
    ]
    destinataire_locataire = models.ForeignKey(
        'locataires.Locataire', on_delete=models.CASCADE,
        related_name='notifications', null=True, blank=True
    )
    loyer = models.ForeignKey(
        'loyers.Loyer', on_delete=models.CASCADE,
        related_name='notifications', null=True, blank=True
    )
    titre = models.CharField(max_length=200)
    message = models.TextField()
    type_notif = models.CharField(max_length=20, choices=TYPE_CHOICES, default='rappel')
    lu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titre