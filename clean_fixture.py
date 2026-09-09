import os
import json
import django
from datetime import datetime, timezone
from collections import defaultdict

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinityhome.settings_test')
django.setup()

from django.apps import apps
from django.db.models import UniqueConstraint


def get_unique_field_names(model):
    """Champs uniques via field.unique=True OU via UniqueConstraint à 1 seul champ."""
    names = {f.name for f in model._meta.get_fields() if getattr(f, "concrete", False) and getattr(f, "unique", False) and not f.primary_key}
    for c in model._meta.constraints:
        if isinstance(c, UniqueConstraint) and len(c.fields) == 1:
            names.add(c.fields[0])
    return names


with open("data_backup.json", encoding="utf-8") as f:
    data = json.load(f)

now_iso = datetime.now(timezone.utc).isoformat()
removed_fields = 0
filled_fields = 0
deduped_fields = 0
skipped_objects = []
unique_counter = 0

# --- Étape 1 : retirer champs obsolètes + combler champs requis manquants ---
for obj in data:
    model_label = obj["model"]
    try:
        model = apps.get_model(model_label)
    except LookupError:
        continue

    valid_field_names = {f.name for f in model._meta.get_fields()}
    fields = obj["fields"]
    unique_names = get_unique_field_names(model)

    for key in list(fields.keys()):
        if key not in valid_field_names:
            del fields[key]
            removed_fields += 1

    for field in model._meta.get_fields():
        if not getattr(field, "concrete", False):
            continue
        if field.primary_key or field.many_to_many:
            continue
        name = field.name
        if name in fields:
            continue
        if getattr(field, "null", True):
            continue
        if field.has_default():
            continue
        if field.auto_created:
            continue

        is_unique = name in unique_names

        if name in ("created_at", "update_at", "updated_at"):
            fields[name] = fields.get("created_at") or now_iso
        elif is_unique:
            unique_counter += 1
            fields[name] = f"__MISSING_{model_label}_{obj.get('pk')}_{unique_counter}"
        elif field.get_internal_type() in ("CharField", "TextField"):
            fields[name] = ""
        elif field.get_internal_type() in ("IntegerField", "FloatField", "DecimalField"):
            fields[name] = 0
        elif field.get_internal_type() == "BooleanField":
            fields[name] = False
        else:
            skipped_objects.append((model_label, obj.get("pk"), name, field.get_internal_type()))
            continue
        filled_fields += 1

# --- Étape 2 : dédupliquer les valeurs existantes sur les champs uniques ---
by_model = defaultdict(list)
for obj in data:
    by_model[obj["model"]].append(obj)

for model_label, objs in by_model.items():
    try:
        model = apps.get_model(model_label)
    except LookupError:
        continue

    unique_field_names = get_unique_field_names(model)

    for fname in unique_field_names:
        seen = {}
        for obj in objs:
            val = obj["fields"].get(fname)
            if val is None:
                continue
            if isinstance(val, (list, dict)):
                continue
            if val not in seen:
                seen[val] = obj
            else:
                unique_counter += 1
                new_val = f"{val}__DUP{unique_counter}" if val else f"__EMPTY_DUP_{unique_counter}"
                obj["fields"][fname] = new_val
                deduped_fields += 1

# --- Étape 3 : corriger la contrainte XOR local/immeuble sur charges.Charge ---
xor_fixed = 0
for obj in data:
    if obj["model"] == "charges.charge":
        fields = obj["fields"]
        if fields.get("local") is not None and fields.get("immeuble") is not None:
            fields["immeuble"] = None  # on garde local, on vide immeuble
            xor_fixed += 1

with open("data_backup.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Champs obsolètes retirés : {removed_fields}")
print(f"Champs requis comblés : {filled_fields}")
print(f"Doublons sur champs uniques corrigés : {deduped_fields}")
print(f"Contrainte XOR local/immeuble corrigée : {xor_fixed}")
if skipped_objects:
    print("⚠️ Champs non résolus automatiquement :")
    for item in skipped_objects:
        print(" -", item)