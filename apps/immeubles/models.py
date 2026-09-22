# apps/immeubles/models.py
from django.db import models

from apps.proprietaires.models import Proprietaire
from apps.immeubles.geo import (
    CONTINENT_CHOICES,
    PAYS_CHOICES,
)


class Immeuble(models.Model):
    # ------------------------------------------------------------------
    # Identité
    # ------------------------------------------------------------------
    nom = models.CharField(max_length=200)

    proprietaire = models.ForeignKey(
        Proprietaire,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='immeubles'
    )

    # ------------------------------------------------------------------
    # Localisation (cascade Continent → Pays → Province → Commune → Quartier)
    # ------------------------------------------------------------------
    continent = models.CharField(
        max_length=50,
        choices=CONTINENT_CHOICES,
        blank=True,
        help_text="Continent de l'immeuble"
    )
    pays = models.CharField(
        max_length=100,
        choices=PAYS_CHOICES,
        blank=True,
        help_text="Pays de l'immeuble"
    )
    adresse_province = models.CharField(
        max_length=100,
        blank=True,
        help_text="Province / région / état"
    )
    adresse_commune = models.CharField(
        max_length=100,
        blank=True,
        help_text="Commune / ville"
    )
    adresse_quartier = models.CharField(
        max_length=100,
        blank=True,
        help_text="Quartier / zone"
    )

    # ------------------------------------------------------------------
    # Complément d'adresse (rue, numéro, etc.)
    # ------------------------------------------------------------------
    adresse_complement = models.CharField(
        max_length=255,
        blank=True,
        help_text="Rue, numéro, avenue, etc."
    )

    # ------------------------------------------------------------------
    # Informations générales
    # ------------------------------------------------------------------
    annee_construction = models.IntegerField(
        null=True, blank=True
    )
    informations_complementaires = models.TextField(blank=True)

    # ------------------------------------------------------------------
    # Timestamps
    # ------------------------------------------------------------------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nom']
        verbose_name = "Immeuble"
        verbose_name_plural = "Immeubles"

    def __str__(self):
        return self.nom

    # ------------------------------------------------------------------
    # Propriétés pratiques (utilisables dans les templates)
    # ------------------------------------------------------------------
    @property
    def adresse_complete(self):
        """Retourne l'adresse lisible, en ignorant les champs vides."""
        parts = [
            self.adresse_complement,
            self.adresse_quartier,
            self.adresse_commune,
            self.adresse_province,
            self.pays,
        ]
        return ", ".join(p for p in parts if p) or "Adresse non renseignée"

    @property
    def localisation_courte(self):
        """Ex : 'Bujumbura, Mukaza, Burundi'."""
        parts = [self.adresse_commune, self.adresse_province, self.pays]
        return ", ".join(p for p in parts if p)