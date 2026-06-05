from django.db import models
# apps/immeubles/models.py
from apps.proprietaires.models import Proprietaire

PROVINCES_COMMUNES = {
    'Bujumbura': ['Mukaza','Ntahangwa','Muha','Kanyosha','Buterere','Gihosha','Ngagara','Rohero','Buyenzi','Bwiza'],
    'Gitega': ['Gitega','Mutumba','Giheta','Itaba','Bugendana','Nyangungu','Ryansoro','Gishubi','Makebuko','Mutaho'],
    'Burunga': ['Burunga','Isare','Mugamba','Matana','Bururi','Songa','Rumonge','Vyanda'],
    'Butanyerera': ['Butanyerera','Gasorwe','Muyinga','Gashoho','Buhinyuza','Butihinda','Giteranyi','Mabayi'],
    'Buhumuza': ['Buhumuza','Kirundo','Busoni','Bugabira','Vumbi','Ntega','Bwambarangwe','Gitobe'],
}
PROVINCE_CHOICES = [(p, p) for p in PROVINCES_COMMUNES.keys()]



class Immeuble(models.Model):
    nom = models.CharField(max_length=200)
    proprietaire = models.ForeignKey(
        Proprietaire,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='immeubles'
    )
    adresse_province = models.CharField(max_length=100, choices=PROVINCE_CHOICES, blank=True)
    adresse_commune = models.CharField(max_length=100, blank=True)
    adresse_quartier = models.CharField(max_length=100, blank=True)
    annee_construction = models.IntegerField(null=True, blank=True)
    informations_complementaires = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.nom
    class Meta:
        ordering = ['nom']