from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [('admin','Administrateur'),('gestionnaire','Gestionnaire'),('lecteur','Lecteur'),('locataire','Locataire'),('proprietaire','Propriétaire')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='lecteur')
    telephone = models.CharField(max_length=30, blank=True)
    locataire_profile = models.OneToOneField('locataires.Locataire', null=True, blank=True, on_delete=models.SET_NULL, related_name='user_account')
    proprietaire_profile = models.OneToOneField('proprietaires.Proprietaire', null=True, blank=True, on_delete=models.SET_NULL, related_name='user_account')
    @property
    def est_admin(self): return self.role == 'admin' or self.is_superuser
    @property
    def peut_ecrire(self): return self.role in ('admin','gestionnaire') or self.is_superuser
    @property
    def full_name(self): return f"{self.first_name} {self.last_name}".strip() or self.username
    def __str__(self): return f"{self.username} ({self.role})"
