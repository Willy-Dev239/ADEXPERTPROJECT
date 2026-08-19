import re
from django.core.management.base import BaseCommand
from apps.loyers.models import Paiement, Bordereau


class Command(BaseCommand):
    help = "Met à jour les Paiement.reference qui pointent encore vers l'ancien format 'Bordereau #<id>' pour utiliser le nouveau Bordereau.numero."

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run', action='store_true',
            help="N'écrit rien, affiche juste ce qui serait fait."
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        pattern = re.compile(r'^Bordereau #(\d+)$')

        paiements = Paiement.objects.filter(reference__startswith='Bordereau #')

        maj = 0
        introuvables = 0

        for p in paiements:
            match = pattern.match(p.reference.strip())
            if not match:
                continue  # référence qui ne suit pas exactement ce format, on ne touche pas

            bordereau_id = int(match.group(1))
            try:
                b = Bordereau.objects.get(pk=bordereau_id)
            except Bordereau.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f"[SKIP] Paiement #{p.id} référence '{p.reference}' → Bordereau #{bordereau_id} introuvable."
                ))
                introuvables += 1
                continue

            if not b.numero:
                self.stdout.write(self.style.WARNING(
                    f"[SKIP] Paiement #{p.id} → Bordereau #{bordereau_id} n'a pas encore de numero."
                ))
                continue

            self.stdout.write(
                f"[{'DRY-RUN' if dry_run else 'FIX'}] Paiement #{p.id} : "
                f"'{p.reference}' → '{b.numero}'"
            )

            if not dry_run:
                p.reference = b.numero
                p.save(update_fields=['reference'])

            maj += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n{'Simulation terminée' if dry_run else 'Terminé'} : "
            f"{maj} paiement(s) {'à corriger' if dry_run else 'corrigé(s)'}, "
            f"{introuvables} bordereau(x) introuvable(s)."
        ))