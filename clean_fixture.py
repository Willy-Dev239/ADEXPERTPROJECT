import json
from datetime import datetime, timezone

with open("data_backup.json", encoding="utf-8") as f:
    data = json.load(f)

now_iso = datetime.now(timezone.utc).isoformat()
fixed = 0

for obj in data:
    fields = obj.get("fields", {})
    # Nettoyage précédent
    if "mot_de_passe_temp" in fields:
        del fields["mot_de_passe_temp"]
    # Nouveau correctif : update_at null -> maintenant (ou created_at si dispo)
    if "update_at" in fields and fields["update_at"] is None:
        fields["update_at"] = fields.get("created_at") or now_iso
        fixed += 1

with open("data_backup.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"update_at corrigé sur {fixed} objet(s)")