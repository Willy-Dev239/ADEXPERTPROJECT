from django.db import models

class Contrat(models.Model):
    STATUT = [('actif','Actif'),('resilie','Résilié'),('expire','Expiré')]
    PERIOD = [('mensuel','Mensuel'),('bimensuel','Bi-mensuel'),('trimestriel','Trimestriel'),('semestriel','Semestriel'),('annuel','Annuel')]
    numero = models.CharField(max_length=50, unique=True)
    locataire = models.ForeignKey('locataires.Locataire', on_delete=models.PROTECT, related_name='contrats')
    local = models.ForeignKey('locaux.Local', on_delete=models.PROTECT, related_name='contrats')
    statut = models.CharField(max_length=20, choices=STATUT, default='actif')
    loyer_hors_charges = models.DecimalField(max_digits=12, decimal_places=2)
    provisions_charges = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    periodicite = models.CharField(max_length=20, choices=PERIOD, default='mensuel')
    depot_garantie = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_entree = models.DateField()
    date_sortie = models.DateField(null=True, blank=True)
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def locataire_nom(self): return self.locataire.nom_prenom
    @property
    def local_reference(self): return self.local.reference
    @property
    def statut_display(self): return dict(self.STATUT).get(self.statut, self.statut)
    @property
    def periodicite_display(self): return dict(self.PERIOD).get(self.periodicite, self.periodicite)
    class Meta:
        ordering = ['-created_at']

class ContratSociete(models.Model):
    STATUT = [('actif','Actif'),('expire','Expiré'),('resilie','Résilié')]
    PERIOD = [('mensuel','Mensuel'),('trimestriel','Trimestriel'),('semestriel','Semestriel')]
    numero = models.CharField(max_length=50, unique=True)
    proprietaire = models.ForeignKey('proprietaires.Proprietaire', on_delete=models.PROTECT, related_name='contrats_societe')
    date_signature = models.DateField()
    date_effet = models.DateField()
    date_expiration = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT, default='actif')
    taux_commission = models.DecimalField(max_digits=5, decimal_places=2, default=9)
    periodicite_reversement = models.CharField(max_length=20, choices=PERIOD, default='mensuel')
    frais_entree = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Feature 7: all services
    service_gestion_loyers = models.BooleanField(default=True)
    service_quittances = models.BooleanField(default=True)
    service_recherche_locataires = models.BooleanField(default=False)
    service_gestion_travaux = models.BooleanField(default=False)
    service_suivi_fiscal = models.BooleanField(default=False)
    service_rapports = models.BooleanField(default=False)
    service_loyers_impayes = models.BooleanField(default=False)
    service_assurances = models.BooleanField(default=False)
    service_judiciaire = models.BooleanField(default=False)
    service_impots_locatifs = models.BooleanField(default=False)
    service_clients = models.BooleanField(default=False)
    service_touristique = models.BooleanField(default=False)
    clauses_particulieres = models.TextField(blank=True)
    notes_internes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def proprietaire_nom(self): return self.proprietaire.nom
    @property
    def statut_display(self): return dict(self.STATUT).get(self.statut, self.statut)
    class Meta:
        ordering = ['-created_at']
