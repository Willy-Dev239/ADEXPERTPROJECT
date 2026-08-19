from django.db import migrations


def backfill_numeros(apps, schema_editor):
    Bordereau = apps.get_model('loyers', 'Bordereau')
    for b in Bordereau.objects.filter(numero__isnull=True).order_by('created_at'):
        annee = b.created_at.year
        dernier = Bordereau.objects.filter(numero__startswith=f'BORD-{annee}-').order_by('-numero').first()
        seq = int(dernier.numero.split('-')[-1]) + 1 if dernier else 1
        b.numero = f'BORD-{annee}-{seq:05d}'
        b.save(update_fields=['numero'])


class Migration(migrations.Migration):

    dependencies = [
        ('loyers', '0004_bordereau_numero'),
    ]

    operations = [
        migrations.RunPython(backfill_numeros, migrations.RunPython.noop),
    ]