import io

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from PIL import Image, UnidentifiedImageError


class Annonce(models.Model):
    STATUT_CHOICES = [
        ('publiee', 'Publiée'),
        ('louee',   'Louée'),
        ('retiree', 'Retirée'),
    ]

    MAX_PHOTOS = 6

    # ------------------------------------------------------------------
    # Relation
    # ------------------------------------------------------------------
    local = models.ForeignKey(
        'locaux.Local',
        on_delete=models.CASCADE,
        related_name='annonces',
    )

    # ------------------------------------------------------------------
    # Contenu affiché publiquement
    # ------------------------------------------------------------------
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    loyer = models.DecimalField(
        max_digits=12, decimal_places=0,
        help_text="Loyer mensuel en BIF",
    )
    contact_telephone = models.CharField(max_length=30)
    contact_whatsapp = models.CharField(max_length=30, blank=True)

    # ------------------------------------------------------------------
    # Statut & dates
    # ------------------------------------------------------------------
    statut = models.CharField(
        max_length=20, choices=STATUT_CHOICES, default='publiee'
    )
    date_publication = models.DateTimeField(default=timezone.now)
    date_retrait = models.DateTimeField(null=True, blank=True)

    # ------------------------------------------------------------------
    # Traçabilité
    # ------------------------------------------------------------------
    publie_par = models.ForeignKey(
        'auth_app.User',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='annonces_publiees',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Annonce"
        verbose_name_plural = "Annonces"

    def __str__(self):
        return f"{self.titre} ({self.local.reference})"

    # ------------------------------------------------------------------
    # Validation : une seule annonce publiée par local
    # (contrainte conditionnelle non supportée par MySQL/MariaDB)
    # ------------------------------------------------------------------
    def clean(self):
        if self.statut == 'publiee':
            doublon = Annonce.objects.filter(
                local=self.local, statut='publiee'
            ).exclude(pk=self.pk)
            if doublon.exists():
                raise ValidationError(
                    "Ce local a déjà une annonce publiée."
                )

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def marquer_louee(self):
        self.statut = 'louee'
        self.date_retrait = timezone.now()
        self.save(update_fields=['statut', 'date_retrait', 'updated_at'])

    def retirer(self):
        self.statut = 'retiree'
        self.date_retrait = timezone.now()
        self.save(update_fields=['statut', 'date_retrait', 'updated_at'])

    # ------------------------------------------------------------------
    # Propriétés pratiques
    # ------------------------------------------------------------------
    @property
    def est_publiee(self):
        return self.statut == 'publiee'

    @property
    def localisation(self):
        return self.local.localisation_courte or self.local.adresse_complete

    @property
    def type_local_display(self):
        return self.local.type_local_display


class AnnoncePhoto(models.Model):
    """Photo stockée en base (compressée en JPEG à l'enregistrement)."""

    MAX_DIMENSION = 1200      # px, côté le plus long
    JPEG_QUALITY = 80
    MAX_UPLOAD_MO = 10        # taille max du fichier envoyé

    annonce = models.ForeignKey(
        Annonce,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    donnees = models.BinaryField(editable=False)
    content_type = models.CharField(max_length=50, default='image/jpeg')
    ordre = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre', 'id']
        verbose_name = "Photo d'annonce"
        verbose_name_plural = "Photos d'annonces"

    def __str__(self):
        return f"Photo {self.ordre} – annonce {self.annonce_id}"

    # ------------------------------------------------------------------
    # Création depuis un fichier uploadé (compression incluse)
    # ------------------------------------------------------------------
    @classmethod
    def depuis_fichier(cls, annonce, fichier, ordre=None):
        if annonce.photos.count() >= Annonce.MAX_PHOTOS:
            raise ValidationError(
                f"Maximum {Annonce.MAX_PHOTOS} photos par annonce."
            )
        if fichier.size > cls.MAX_UPLOAD_MO * 1024 * 1024:
            raise ValidationError(
                f"Fichier trop volumineux (max {cls.MAX_UPLOAD_MO} Mo)."
            )

        try:
            img = Image.open(fichier)
            img.load()
        except (UnidentifiedImageError, OSError):
            raise ValidationError("Le fichier n'est pas une image valide.")

        # Conversion en RGB (gère PNG transparents, HEIC->JPEG, etc.)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.thumbnail((cls.MAX_DIMENSION, cls.MAX_DIMENSION))

        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=cls.JPEG_QUALITY, optimize=True)

        if ordre is None:
            ordre = annonce.photos.count()

        return cls.objects.create(
            annonce=annonce,
            donnees=buffer.getvalue(),
            content_type='image/jpeg',
            ordre=ordre,
        )