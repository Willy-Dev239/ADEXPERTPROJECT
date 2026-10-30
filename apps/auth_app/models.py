from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone


class EmailVerification(models.Model):
    TTL = timedelta(minutes=10)
    MAX_ATTEMPTS = 5

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='email_verification')
    code_hash = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    attempts = models.PositiveSmallIntegerField(default=0)

    @classmethod
    def issue(cls, user):
        code = f"{secrets.randbelow(10**6):06d}"
        cls.objects.update_or_create(user=user, defaults={
            'code_hash': make_password(code),
            'created_at': timezone.now(),
            'attempts': 0,
        })
        return code

    def is_expired(self):
        return timezone.now() > self.created_at + self.TTL

    def verify_code(self, code):
        if self.is_expired() or self.attempts >= self.MAX_ATTEMPTS:
            return False
        if check_password(code, self.code_hash):
            return True
        self.attempts += 1
        self.save(update_fields=['attempts'])
        return False
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


