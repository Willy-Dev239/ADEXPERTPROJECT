from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint


class Proprietaire(models.Model):
    nom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    adresse_province = models.CharField(max_length=100, blank=True)
    adresse_commune = models.CharField(max_length=100, blank=True)
    adresse_quartier = models.CharField(max_length=100, blank=True)
    activation_token = models.CharField(max_length=128, blank=True, null=True, unique=True)
    expiration_token = models.DateTimeField(null=True, blank=True)
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def nb_locaux(self): return self.locaux.count()

    def generer_token_activation(self, duree_heures=48):
        """Génère un jeton d'activation sécurisé et sa date d'expiration."""
        self.activation_token = secrets.token_urlsafe(32)
        self.expiration_token = timezone.now() + timedelta(hours=duree_heures)
        self.save(update_fields=['activation_token', 'expiration_token'])
        return self.activation_token

    def token_est_valide(self, token):
        """Vérifie que le jeton fourni correspond et n'a pas expiré."""
        return (
            self.activation_token
            and self.activation_token == token
            and self.expiration_token
            and timezone.now() < self.expiration_token
        )

    def invalider_token(self):
        """Consomme le jeton après activation réussie."""
        self.activation_token = None
        self.expiration_token = None
        self.save(update_fields=['activation_token', 'expiration_token'])

    def clean(self):
        self.email = self.email.strip().lower() if self.email else None
        self.telephone = (
            self.telephone.strip().replace(' ', '').replace('-', '')
            if self.telephone else None
        )

        if self.email:
            conflit = Proprietaire.objects.filter(email=self.email).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'email': "Un propriétaire utilise déjà cet email."})

        if self.telephone:
            conflit = Proprietaire.objects.filter(telephone=self.telephone).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'telephone': "Un propriétaire utilise déjà ce téléphone."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self): return self.nom

    class Meta:
        ordering = ['nom']
        constraints = [
            UniqueConstraint(fields=['email'], name='uniq_proprietaire_email'),
            UniqueConstraint(fields=['telephone'], name='uniq_proprietaire_telephone'),
        ]