from django.db import models
class Proprietaire(models.Model):
    nom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    adresse_province = models.CharField(max_length=100, blank=True)
    adresse_commune = models.CharField(max_length=100, blank=True)
    adresse_quartier = models.CharField(max_length=100, blank=True)
    mot_de_passe_temp = models.CharField(max_length=128, blank=True, default='')
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def nb_locaux(self): return self.locaux.count()
    def __str__(self): return self.nom
    class Meta:
        ordering = ['nom']
