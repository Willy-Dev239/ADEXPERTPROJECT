# apps/proprietaires/models.py
import secrets
from datetime import timedelta

from django.db import models
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.immeubles.geo import CONTINENT_CHOICES, PAYS_CHOICES


class Proprietaire(models.Model):
    # ------------------------------------------------------------------
    # Identité
    # ------------------------------------------------------------------
    nom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nif = models.CharField(max_length=30, blank=True, null=True, unique=True)
    cni = models.CharField(max_length=30, blank=True, null=True)

    # ------------------------------------------------------------------
    # Localisation en cascade
    # ------------------------------------------------------------------
    continent = models.CharField(
        max_length=50, choices=CONTINENT_CHOICES, blank=True,
        help_text="Continent du propriétaire"
    )
    pays = models.CharField(
        max_length=100, choices=PAYS_CHOICES, blank=True,
        help_text="Pays du propriétaire"
    )
    adresse_province = models.CharField(max_length=100, blank=True)
    adresse_commune = models.CharField(max_length=100, blank=True)
    adresse_quartier = models.CharField(max_length=100, blank=True)

    # ------------------------------------------------------------------
    # Token d'activation
    # ------------------------------------------------------------------
    activation_token = models.CharField(max_length=128, blank=True, null=True, unique=True)
    expiration_token = models.DateTimeField(null=True, blank=True)

    # ------------------------------------------------------------------
    # Compléments
    # ------------------------------------------------------------------
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ------------------------------------------------------------------
    # Propriétés
    # ------------------------------------------------------------------
    @property
    def nb_locaux(self):
        return self.locaux.count()

    @property
    def adresse_complete(self):
        parts = [
            self.adresse_quartier,
            self.adresse_commune,
            self.adresse_province,
            self.pays,
        ]
        return ", ".join(p for p in parts if p) or "Adresse non renseignée"

    @property
    def localisation_courte(self):
        parts = [self.adresse_commune, self.adresse_province, self.pays]
        return ", ".join(p for p in parts if p)

    # ------------------------------------------------------------------
    # Tokens
    # ------------------------------------------------------------------
    def generer_token_activation(self, duree_heures=48):
        self.activation_token = secrets.token_urlsafe(32)
        self.expiration_token = timezone.now() + timedelta(hours=duree_heures)
        self.save(update_fields=['activation_token', 'expiration_token'])
        return self.activation_token

    def token_est_valide(self, token):
        return (
            self.activation_token
            and self.activation_token == token
            and self.expiration_token
            and timezone.now() < self.expiration_token
        )

    def invalider_token(self):
        self.activation_token = None
        self.expiration_token = None
        self.save(update_fields=['activation_token', 'expiration_token'])

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def clean(self):
        self.email = self.email.strip().lower() if self.email else None
        self.telephone = (
            self.telephone.strip().replace(' ', '').replace('-', '')
            if self.telephone else None
        )
        self.nif = self.nif.strip() if self.nif else None
        self.cni = self.cni.strip() if self.cni else None

        if self.email:
            conflit = Proprietaire.objects.filter(email=self.email).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'email': "Un propriétaire utilise déjà cet email."})

        if self.telephone:
            conflit = Proprietaire.objects.filter(telephone=self.telephone).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'telephone': "Un propriétaire utilise déjà ce téléphone."})

        if self.nif:
            conflit = Proprietaire.objects.filter(nif=self.nif).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'nif': "Un propriétaire utilise déjà ce NIF."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['nom']
        verbose_name = "Propriétaire"
        verbose_name_plural = "Propriétaires"
        constraints = [
            UniqueConstraint(fields=['email'], name='uniq_proprietaire_email'),
            UniqueConstraint(fields=['telephone'], name='uniq_proprietaire_telephone'),
            UniqueConstraint(fields=['nif'], name='uniq_proprietaire_nif'),
        ]