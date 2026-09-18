from django.db import models
# apps/immeubles/models.py
from apps.proprietaires.models import Proprietaire

PROVINCES_COMMUNES_QUARTIERS = {
    'Buhumuza': {
        'Butaganzwa': ['Buhumuza','Gitega','Kinyinya','Mukinya'],
        'Butihinda':  ['Butihinda','Kabanga','Kigoma','Muyange'],
        'Cankuzo':    ['Cankuzo','Gisagara','Kigamba','Nyamugari'],
        'Gisagara':   ['Gisagara','Kigamba','Mukanda','Nyarusange'],
        'Gisuru':     ['Gisuru','Kinyinya','Mukuyi','Nyabitare'],
        'Muyinga':    ['Muyinga','Buhinyuza','Gashoho','Giteranyi'],
        'Ruyigi':     ['Ruyigi','Bweru','Butezi','Kinyinya'],
    },
    'Bujumbura': {
        'Bubanza':      ['Bubanza','Gihanga','Mpanda','Musigati','Rugazi'],
        'Bukinanyana':  ['Bukinanyana','Mabayi','Mugongomanga','Ruhororo'],
        'Cibitoke':     ['Cibitoke','Buganda','Mabayi','Murwi','Rugombo'],
        'Isare':        ['Isare','Kabezi','Mubimbi','Mutimbuzi'],
        'Mpanda':       ['Mpanda','Gihanga','Matongo','Mugongomanga'],
        'Mugere':       ['Mugere','Kanyosha','Kinama','Muha'],
        'Mugina':       ['Mugina','Kabezi','Mutimbuzi','Nyanza-Lac'],
        'Muhuta':       ['Muhuta','Kabezi','Mubimbi','Mutimbuzi'],
        'Mukaza':       ['Rohero','Kiriri','Buyenzi','Bwiza','Nyakabiga'],
        'Ntahangwa':    ['Ngagara','Cibitoke','Kamenge','Kinama','Gihosha'],
        'Rwibaga':      ['Rwibaga','Gatumba','Mutimbuzi','Nyanza-Lac'],
    },
    'Burunga': {
        'Bururi':     ['Bururi','Matana','Mugamba','Rutovu','Songa'],
        'Makamba':    ['Makamba','Kayogoro','Kibago','Mabanda','Vugizo'],
        'Matana':     ['Matana','Bururi','Mugamba','Rutovu'],
        'Musongati':  ['Musongati','Nyanza-Lac','Rutana','Vugizo'],
        'Nyanza':     ['Nyanza','Bugarama','Matana','Nyabihanga'],
        'Rumonge':    ['Rumonge','Burambi','Buyengero','Muhuta'],
        'Rutana':     ['Rutana','Bukemba','Giharo','Gitanga'],
    },
    'Butanyerera': {
        'Busoni':     ['Busoni','Bugabira','Bwambarangwe','Kirundo'],
        'Kayanza':    ['Kayanza','Gahombo','Gatara','Kabaro','Matongo'],
        'Kiremba':    ['Kiremba','Buhiga','Gahombo','Gatara'],
        'Kirundo':    ['Kirundo','Bugabira','Busoni','Gitobe','Vumbi'],
        'Matongo':    ['Matongo','Gahombo','Kayanza','Muruta'],
        'Muhanga':    ['Muhanga','Bukeye','Kayanza','Rango'],
        'Ngozi':      ['Ngozi','Gahombo','Kiremba','Marangara','Tangara'],
        'Tangara':    ['Tangara','Kiremba','Mwumba','Ngozi'],
    },
    'Gitega': {
        'Bugendana':  ['Bugendana','Buraza','Gitega','Makebuko'],
        'Gishubi':    ['Gishubi','Bugendana','Gitega','Nyarusange'],
        'Gitega':     ['Gitega','Bugendana','Gishubi','Makebuko'],
        'Kiganda':    ['Kiganda','Bugendana','Muramvya','Ruyigi'],
        'Muramvya':   ['Muramvya','Bukeye','Kiganda','Mwaro'],
        'Mwaro':      ['Mwaro','Bisoro','Gisozi','Kayokwe'],
        'Nyabihanga': ['Nyabihanga','Gitega','Nyanza','Shombo'],
        'Shombo':     ['Shombo','Buraza','Gitega','Nyarusange'],
    },
}

PROVINCES_COMMUNES = {
    prov: list(communes.keys())
    for prov, communes in PROVINCES_COMMUNES_QUARTIERS.items()
}
PROVINCE_CHOICES = [(p, p) for p in PROVINCES_COMMUNES_QUARTIERS.keys()]

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