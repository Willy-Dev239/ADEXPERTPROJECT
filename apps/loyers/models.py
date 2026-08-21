from django.db import models
from django.utils import timezone
from pyuploadcare.dj.models import ImageField
from apps.core.models import SoftDeleteModel
class Loyer(SoftDeleteModel):
    STATUT = [
        ('attente', 'En attente'),
        ('partiel', 'Partiellement payé'),
        ('paye', 'Payé'),
        ('retard', 'En retard'),
        ('annule', 'Annulé'),
    ]

    contrat = models.ForeignKey(
        'contrats.Contrat',
        on_delete=models.PROTECT,
        null=False, blank=False,
        related_name='loyers'
    )
    locataire = models.ForeignKey(
        'locataires.Locataire', on_delete=models.PROTECT,
        related_name='loyers', editable=False
    )
    local = models.ForeignKey(
        'locaux.Local', on_delete=models.PROTECT,
        related_name='loyers', editable=False
    )
    libelle = models.CharField(max_length=200)
    periode_debut = models.DateField()
    periode_fin = models.DateField(null=True, blank=True)
    loyer_hors_charges = models.DecimalField(max_digits=12, decimal_places=2)
    charges = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    echeance = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT, default='attente')
    quittance_envoyee = models.BooleanField(default=False)
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='Loyers_crees')
    validated_by = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, related_name='Loyers_valides')
    update_at = models.DateTimeField(auto_now=True)

    @property
    def montant_total(self): return self.loyer_hors_charges + self.charges
    @property
    def montant_paye(self): return sum(p.montant for p in self.paiements.filter(annule=False))
    @property
    def solde_restant(self): return self.montant_total - self.montant_paye
    @property
    def locataire_nom(self): return self.locataire.nom_prenom
    @property
    def local_reference(self): return self.local.reference

    def get_statut_display_custom(self): return dict(self.STATUT).get(self.statut, self.statut)

    def update_statut(self):
        if self.statut == 'annule':
            return  # un loyer annulé ne doit pas être recalculé automatiquement
        p = self.montant_paye; t = self.montant_total
        if p >= t: self.statut = 'paye'
        elif p > 0: self.statut = 'partiel'
        elif timezone.now().date() > self.echeance: self.statut = 'retard'
        else: self.statut = 'attente'
        self.save(update_fields=['statut'])

    def save(self, *args, **kwargs):
        if self.contrat_id:
            self.local_id = self.contrat.local_id
            self.locataire_id = self.contrat.locataire_id
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-echeance']
class Paiement(models.Model):
    MODE = [('especes','Espèces'),('virement','Virement'),('cheque','Chèque'),('mobile_money','Mobile Money'),('autre','Autre')]
    STATUT_VALIDATION = [('en_attente', 'En attente'), ('valide', 'Validé')]

    loyer = models.ForeignKey(Loyer, on_delete=models.CASCADE, related_name='paiements')
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    date_paiement = models.DateField()
    mode_paiement = models.CharField(max_length=20, choices=MODE, default='especes')
    reference = models.CharField(max_length=100, blank=True)
    reference_transaction = models.CharField(max_length=100, blank=True, help_text="Référence bancaire / mobile money de la transaction")
    banque_operateur = models.CharField(max_length=100, blank=True, help_text="Nom de la banque ou de l'opérateur mobile money")
    encaisse_par = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='paiements_encaisses')
    statut_validation = models.CharField(max_length=20, choices=STATUT_VALIDATION, default='en_attente')
    date_validation = models.DateTimeField(null=True, blank=True)
    commentaire = models.TextField(blank=True)
    annule = models.BooleanField(default=False)
    date_annulation = models.DateTimeField(null=True, blank=True)
    annule_par = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='paiements_annules')
    motif_annulation = models.TextField(blank=True)
    created_by = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='paiements_crees')
    validated_by = models.ForeignKey('auth_app.User', on_delete=models.SET_NULL, null=True, related_name='paiements_valides')
    update_at = models.DateTimeField(auto_now=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def montant_paye(self): return sum(p.montant for p in self.paiements.filter(annule=False))
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.loyer.update_statut()

    class Meta:
        ordering = ['-date_paiement']
from pyuploadcare.dj.models import ImageField
import re

UUID_RE = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
    re.IGNORECASE
)
class Bordereau(models.Model):
    STATUT = [('en_attente','En attente'),('valide','Validé'),('rejete','Rejeté')]
    numero = models.CharField(max_length=30, unique=True, blank=True, null=True, editable=False)
    locataire = models.ForeignKey('locataires.Locataire', on_delete=models.CASCADE, related_name='bordereaux')
    loyer = models.ForeignKey(Loyer, on_delete=models.SET_NULL, null=True, blank=True, related_name='bordereaux')
    photo = ImageField(blank=True, null=True)
    notes = models.TextField(blank=True)
    reference_client = models.CharField(
        max_length=100, blank=True,
        help_text="Référence de transaction saisie par le locataire (n° Mobile Money, virement, chèque, etc.)"
    )
    statut = models.CharField(max_length=20, choices=STATUT, default='en_attente')
    commentaire_admin = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.numero:
            annee = timezone.now().year
            dernier = Bordereau.objects.filter(numero__startswith=f'BORD-{annee}-').order_by('-numero').first()
            if dernier:
                dernier_seq = int(dernier.numero.split('-')[-1])
            else:
                dernier_seq = 0
            self.numero = f'BORD-{annee}-{dernier_seq + 1:05d}'
        super().save(*args, **kwargs)

    @classmethod
    def from_db(cls, db, field_names, values):
        if 'photo' in field_names:
            idx = list(field_names).index('photo')
            val = values[idx]
            if val and not UUID_RE.match(str(val).strip()):
                values = list(values)
                values[idx] = None
                values = tuple(values)
        return super().from_db(db, field_names, values)