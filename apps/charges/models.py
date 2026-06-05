from django.db import models

class Charge(models.Model):
    TYPE_CHOICES = [
        ('travaux','Travaux/Entretien'),('impot_locatif','Impôt locatif'),
        ('impot_foncier','Taxe foncière'),('frais_cabinet','Frais cabinet'),
        ('arrieres','Arriérés'),('assurance','Assurance'),
        ('eau_electricite','Eau/Électricité'),('autre','Autre'),
    ]
    libelle = models.CharField(max_length=200)
    type_charge = models.CharField(max_length=30, choices=TYPE_CHOICES, default='autre')
    local = models.ForeignKey('locaux.Local', on_delete=models.SET_NULL, null=True, blank=True, related_name='charges')
    immeuble = models.ForeignKey('immeubles.Immeuble', on_delete=models.SET_NULL, null=True, blank=True, related_name='charges')
    montant_ttc = models.DecimalField(max_digits=12, decimal_places=2)
    date_charge = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def local_reference(self): return self.local.reference if self.local else None
    @property
    def immeuble_nom(self): return self.immeuble.nom if self.immeuble else None
    @property
    def type_display(self): return dict(self.TYPE_CHOICES).get(self.type_charge, self.type_charge)
    class Meta:
        ordering = ['-date_charge']
