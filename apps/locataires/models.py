from django.db import models


class Locataire(models.Model):
    nom_prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
  
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
    def __str__(self): return self.nom_prenom
    class Meta:
        ordering = ['nom_prenom']
