from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint


class Locataire(models.Model):
    nom_prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    adresse_postale = models.CharField(max_length=300, blank=True)
    informations_complementaires = models.TextField(blank=True)
    mot_de_passe_temp = models.CharField(max_length=128, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def local_actuel(self):
        c = self.contrats.filter(statut='actif').first()
        return c.local if c else None

    @property
    def situation_financiere(self):
        loyers = self.loyers.all()
        total = sum(float(l.montant_total) for l in loyers)
        paye = sum(float(l.montant_paye) for l in loyers)
        retard = loyers.filter(statut='retard').count()
        return {'total_loyers': total, 'montant_paye': paye, 'solde_restant': total - paye, 'loyers_en_retard': retard}

    def clean(self):
        # Normalisation : chaîne vide -> None, pour que MariaDB
        # laisse passer plusieurs locataires "sans email/téléphone"
        self.email = self.email.strip().lower() if self.email else None
        self.telephone = (
            self.telephone.strip().replace(' ', '').replace('-', '')
            if self.telephone else None
        )

        if self.email:
            conflit = Locataire.objects.filter(email=self.email).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'email': "Un locataire utilise déjà cet email."})

        if self.telephone:
            conflit = Locataire.objects.filter(telephone=self.telephone).exclude(pk=self.pk)
            if conflit.exists():
                raise ValidationError({'telephone': "Un locataire utilise déjà ce téléphone."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self): return self.nom_prenom

    class Meta:
        ordering = ['nom_prenom']
        constraints = [
            UniqueConstraint(fields=['email'], name='uniq_locataire_email'),
            UniqueConstraint(fields=['telephone'], name='uniq_locataire_telephone'),
        ]