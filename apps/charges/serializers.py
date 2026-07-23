from django.utils import timezone
from datetime import timedelta
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError
from apps.charges.models import Charge


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'

    def validate(self, data):
        local = data.get('local', getattr(self.instance, 'local', None))
        immeuble = data.get('immeuble', getattr(self.instance, 'immeuble', None))

        # ── Règle XOR : un et un seul des deux doit être renseigné ──
        if bool(local) == bool(immeuble):
            raise DRFValidationError(
                "Une charge doit concerner soit un local, soit un immeuble, "
                "mais pas les deux ni aucun des deux."
            )

        # ── Détection de double soumission ──
        fenetre = timezone.now() - timedelta(seconds=10)
        doublon = Charge.objects.filter(
            libelle=data.get('libelle'),
            montant_ttc=data.get('montant_ttc'),
            date_charge=data.get('date_charge'),
            local=local,
            immeuble=immeuble,
            created_at__gte=fenetre,
        )
        if self.instance:
            doublon = doublon.exclude(pk=self.instance.pk)
        if doublon.exists():
            raise DRFValidationError(
                "Une charge identique vient d'être enregistrée. "
                "Vérifiez qu'il ne s'agit pas d'une double soumission."
            )

        return data