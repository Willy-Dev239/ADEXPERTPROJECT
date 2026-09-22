# apps/locaux/models.py
from django.db import models

from apps.immeubles.geo import (
    CONTINENT_CHOICES,
    PAYS_CHOICES,
)


class Local(models.Model):
    # ------------------------------------------------------------------
    # Types & statuts
    # ------------------------------------------------------------------
    TYPE_CHOICES = [
        ('appartement', 'Appartement'),
        ('maison',      'Maison'),
        ('bureau',      'Bureau'),
        ('commerce',    'Commerce'),
        ('garage',      'Garage'),
        ('autre',       'Autre'),
    ]
    STATUT_CHOICES = [
        ('libre',       'Libre'),
        ('occupe',      'Occupé'),
        ('reserve',     'Réservé'),
        ('maintenance', 'En maintenance'),
    ]

    # ------------------------------------------------------------------
    # Identité
    # ------------------------------------------------------------------
    reference = models.CharField(max_length=50, unique=True)
    type_local = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='appartement'
    )
    statut = models.CharField(
        max_length=20, choices=STATUT_CHOICES, default='libre'
    )

    # ------------------------------------------------------------------
    # Relations
    # ------------------------------------------------------------------
    proprietaire = models.ForeignKey(
        'proprietaires.Proprietaire',
        on_delete=models.PROTECT,
        related_name='locaux',
    )
    immeuble = models.ForeignKey(
        'immeubles.Immeuble',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='locaux',
    )

    # ------------------------------------------------------------------
    # Localisation en cascade
    # ------------------------------------------------------------------
    continent = models.CharField(
        max_length=50, choices=CONTINENT_CHOICES, blank=True,
        help_text="Continent du local"
    )
    pays = models.CharField(
        max_length=100, choices=PAYS_CHOICES, blank=True,
        help_text="Pays du local"
    )
    adresse_province = models.CharField(max_length=100, blank=True)
    adresse_commune = models.CharField(max_length=100, blank=True)
    adresse_quartier = models.CharField(max_length=100, blank=True)

    # ------------------------------------------------------------------
    # Caractéristiques
    # ------------------------------------------------------------------
    superficie = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    annee_construction = models.IntegerField(null=True, blank=True)
    meuble = models.BooleanField(default=False)
    informations_complementaires = models.TextField(blank=True)

    # ------------------------------------------------------------------
    # Traçabilité
    # ------------------------------------------------------------------
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        'auth_app.User',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='locaux_crees',
    )
    validated_by = models.ForeignKey(
        'auth_app.User',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='locaux_valides',
    )

    # ------------------------------------------------------------------
    # Propriétés
    # ------------------------------------------------------------------
    @property
    def est_occupe(self):
        return self.contrats.filter(statut='actif').exists()

    @property
    def proprietaire_nom(self):
        return self.proprietaire.nom

    @property
    def type_local_display(self):
        return dict(self.TYPE_CHOICES).get(self.type_local, self.type_local)

    @property
    def statut_display(self):
        return dict(self.STATUT_CHOICES).get(self.statut, self.statut)

    @property
    def adresse_complete(self):
        parts = [
            self.adresse_quartier,
            self.adresse_commune,
            self.adresse_province,
            self.pays,
        ]
        return ', '.join(p for p in parts if p) or "Adresse non renseignée"

    @property
    def localisation_courte(self):
        parts = [self.adresse_commune, self.adresse_province, self.pays]
        return ', '.join(p for p in parts if p)

    def __str__(self):
        return f"{self.reference}"

    class Meta:
        ordering = ['reference']
        verbose_name = "Local"
        verbose_name_plural = "Locaux"