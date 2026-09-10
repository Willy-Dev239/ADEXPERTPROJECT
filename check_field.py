import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinityhome.settings_test')
django.setup()

from django.apps import apps

model = apps.get_model('locataires.locataire')
f = model._meta.get_field('telephone')
print('unique:', f.unique)
print('constraints:', model._meta.constraints)
print('unique_together:', model._meta.unique_together)
print('indexes:', [(i.fields, getattr(i, 'unique', None)) for i in model._meta.indexes])