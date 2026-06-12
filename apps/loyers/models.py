from django.db import models
from django.utils import timezone
from pyuploadcare.dj.models import ImageField
class Loyer(models.Model):
    STATUT = [('attente','En attente'),('partiel','Partiel'),('paye','Payé'),('retard','En retard')]
    contrat = models.ForeignKey('contrats.Contrat', on_delete=models.SET_NULL, null=True, blank=True, related_name='loyers')
    locataire = models.ForeignKey('locataires.Locataire', on_delete=models.PROTECT, related_name='loyers')
    local = models.ForeignKey('locaux.Local', on_delete=models.PROTECT, related_name='loyers')
    libelle = models.CharField(max_length=200)
    periode_debut = models.DateField()
    periode_fin = models.DateField(null=True, blank=True)
    loyer_hors_charges = models.DecimalField(max_digits=12, decimal_places=2)
    charges = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    echeance = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT, default='attente')
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def montant_total(self): return self.loyer_hors_charges + self.charges
    @property
    def montant_paye(self): return sum(p.montant for p in self.paiements.all())
    @property
    def solde_restant(self): return self.montant_total - self.montant_paye
    @property
    def locataire_nom(self): return self.locataire.nom_prenom
    @property
    def local_reference(self): return self.local.reference
    def get_statut_display_custom(self): return dict(self.STATUT).get(self.statut, self.statut)
    def update_statut(self):
        p = self.montant_paye; t = self.montant_total
        if p >= t: self.statut = 'paye'
        elif p > 0: self.statut = 'partiel'
        elif timezone.now().date() > self.echeance: self.statut = 'retard'
        else: self.statut = 'attente'
        self.save(update_fields=['statut'])
    class Meta:
        ordering = ['-echeance']

class Paiement(models.Model):
    MODE = [('especes','Espèces'),('virement','Virement'),('cheque','Chèque'),('mobile_money','Mobile Money'),('autre','Autre')]
    loyer = models.ForeignKey(Loyer, on_delete=models.CASCADE, related_name='paiements')
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    date_paiement = models.DateField()
    mode_paiement = models.CharField(max_length=20, choices=MODE, default='especes')
    reference = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.loyer.update_statut()
    class Meta:
        ordering = ['-date_paiement']

class Bordereau(models.Model):
    STATUT = [('en_attente','En attente'),('valide','Validé'),('rejete','Rejeté')]
    locataire = models.ForeignKey('locataires.Locataire', on_delete=models.CASCADE, related_name='bordereaux')
    loyer = models.ForeignKey(Loyer, on_delete=models.SET_NULL, null=True, blank=True, related_name='bordereaux')
    
    photo = ImageField(blank=True, null=True)
    notes = models.TextField(blank=True)
    statut = models.CharField(max_length=20, choices=STATUT, default='en_attente')
    commentaire_admin = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
