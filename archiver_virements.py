"""
Script d'archivage local des bordereaux de virement ADEXPERT.

Télécharge tous les bordereaux (via l'API Django) et les classe sur le disque :
    media/archives_virements/{Propriétaire}/{AAAA-MM}/{date}_{reference}.ext

Prérequis :
    pip install requests --break-system-packages   (ou dans ta venv Windows)

Utilisation :
    1. Renseigne TOKEN ci-dessous (token d'un compte admin ou gestionnaire,
       pour voir TOUS les bordereaux — pas seulement ceux d'un propriétaire).
    2. Lance : python archiver_virements.py
"""

import os
import re
import requests
from datetime import datetime

# ── CONFIGURATION ──────────────────────────────────────────────
BASE_URL = "https://adexpert-app.onrender.com/api"
TOKEN = "a9e68734f9bb89314490a5dc02d98a1e9dc9fc26" 
OUTPUT_DIR = r"D:\Ma BIBLIOTHEQUE\Websites\gestion_locative\infinityhome\media\archives_virements"
# ────────────────────────────────────────────────────────────────

HEADERS = {"Authorization": f"Token {TOKEN}"}


def safe_name(s):
    """Nettoie un nom pour l'utiliser comme nom de dossier/fichier Windows."""
    s = str(s or "Inconnu").strip()
    return re.sub(r'[\\/*?:"<>|]', "_", s) or "Inconnu"


def get_all_virements():
    """Récupère tous les bordereaux, en suivant la pagination DRF."""
    virements = []
    url = f"{BASE_URL}/contrats/bordereaux-virement/?page_size=100"
    while url:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, dict):
            virements.extend(data.get("results", []))
            url = data.get("next")
        else:
            virements.extend(data)
            url = None
    return virements


def get_proprietaire_nom(v):
    """Essaie plusieurs clés possibles selon ce que renvoie ton serializer."""
    for key in ("proprietaire_nom", "contrat_proprietaire_nom", "proprietaire", "contrat_numero"):
        if v.get(key):
            return v[key]
    return "Inconnu"


def download_file(url, dest_path):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)


def main():
    if "COLLE_TON_TOKEN" in TOKEN:
        print("⚠️  Renseigne d'abord ton TOKEN admin en haut du script.")
        return

    print("Récupération de la liste des bordereaux...")
    virements = get_all_virements()
    print(f"{len(virements)} bordereau(x) trouvé(s).\n")

    nb_ok, nb_skip, nb_err = 0, 0, 0

    for v in virements:
        prop = safe_name(get_proprietaire_nom(v))
        date_str = v.get("date_virement") or ""
        try:
            mois = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m")
        except Exception:
            mois = "date_inconnue"

        folder = os.path.join(OUTPUT_DIR, prop, mois)
        os.makedirs(folder, exist_ok=True)

        fichier_url = v.get("fichier_url")
        if not fichier_url:
            continue

        ext = os.path.splitext(fichier_url.split("?")[0])[1] or ".pdf"
        ref = safe_name(v.get("reference_virement") or v.get("id") or "sans_ref")
        filename = f"{date_str}_{ref}{ext}"
        dest = os.path.join(folder, filename)

        if os.path.exists(dest):
            nb_skip += 1
            continue

        try:
            download_file(fichier_url, dest)
            print(f"✅ {dest}")
            nb_ok += 1
        except Exception as e:
            print(f"❌ Erreur pour {fichier_url} : {e}")
            nb_err += 1

    print(f"\nTerminé. {nb_ok} téléchargé(s), {nb_skip} déjà présent(s), {nb_err} erreur(s).")


if __name__ == "__main__":
    main()
