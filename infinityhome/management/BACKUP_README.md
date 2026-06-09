# 🗄️ Système de Backup — InfinityHome / ADEXPERT

## 📁 Structure à créer dans ton projet

```
infinityhome/          ← ton projet Django
├── backups/           ← dossier créé automatiquement
│   ├── logs/          ← logs de chaque backup
│   ├── infinityhome_backup_20260601_143000.zip
│   └── infinityhome_backup_20260601_120000.zip
├── infinityhome/      ← ton app Django principale
│   └── management/
│       └── commands/
│           └── backup.py   ← LA COMMANDE À COPIER ICI
├── backup.sh          ← script bash (optionnel)
└── manage.py
```

---

## ⚙️ Installation

### Étape 1 — Copier les fichiers

```bash
# Copier la commande Django
cp backup.py  ton_projet/infinityhome/management/commands/backup.py

# Copier le script bash (optionnel)
cp backup.sh  ton_projet/backup.sh
chmod +x      ton_projet/backup.sh
```

### Étape 2 — Vérifier les __init__.py

```bash
# Ces fichiers doivent exister (peuvent être vides)
touch infinityhome/management/__init__.py
touch infinityhome/management/commands/__init__.py
```

### Étape 3 — Vérifier settings.py

```python
# settings.py — ta config MySQL doit ressembler à ça :
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adexpert_recouvrement_db',
        'USER': 'adexpert',           # Modifier selon votre config MySQL
        'PASSWORD': 'adexpert2121',  # Modifier
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Et MEDIA_ROOT doit être défini :
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🚀 Utilisation

### Backup complet (BDD + Media + Code)
```bash
python manage.py backup
```

### Backup base de données uniquement
```bash
python manage.py backup --db-only
```

### Backup fichiers media uniquement
```bash
python manage.py backup --media-only
```

### Backup code source uniquement
```bash
python manage.py backup --code-only
```

### Lister les backups existants
```bash
python manage.py backup --list
```

### Supprimer les anciens (garder les 10 derniers)
```bash
python manage.py backup --clean --keep 10
```

### Sauvegarder dans un dossier personnalisé
```bash
python manage.py backup --output /home/user/mes_backups
```

### Restaurer un backup
```bash
python manage.py backup --restore infinityhome_backup_20260601_143000
```

---

## 📦 Contenu d'un fichier ZIP de backup

```
infinityhome_backup_20260601_143000.zip
├── database_20260601_143000.sql       ← dump MySQL complet
├── media_20260601_143000.zip          ← tous les fichiers media
├── code_20260601_143000.zip           ← code source (sans venv/cache)
└── backup_meta.json                   ← métadonnées du backup
```

---

## ⏰ Automatisation (optionnel)

### Via cron (Linux/Mac)
```bash
crontab -e

# Backup tous les jours à 2h du matin
0 2 * * * cd /chemin/vers/ton/projet && python manage.py backup --db-only >> backups/logs/cron.log 2>&1

# Backup complet tous les dimanches à 3h
0 3 * * 0 cd /chemin/vers/ton/projet && python manage.py backup >> backups/logs/cron.log 2>&1
```

### Via le script bash
```bash
# Backup complet
./backup.sh

# Backup BDD seulement
./backup.sh --db-only

# Lister
./backup.sh --list
```

---

## 🔧 Dépendances requises

- `mysqldump` installé sur le serveur (client MySQL)
- Python 3.8+
- Django 3.2+

### Vérifier que mysqldump est disponible
```bash
mysqldump --version
# mysqldump  Ver 8.0.xx ...
```

### Si mysqldump n'est pas disponible
La commande utilise automatiquement le **fallback Django** (`dumpdata`) qui sauvegarde en JSON. Moins optimal mais fonctionnel.

---

## 🔄 Restauration

```bash
# 1. Lister les backups
python manage.py backup --list

# 2. Restaurer (remplacer par le vrai nom)
python manage.py backup --restore infinityhome_backup_20260601_143000

# ⚠️ Une confirmation manuelle "OUI" est demandée avant d'écraser la BDD
```

---

## 📊 Exemple de sortie

```
═════════════════════════════════════════════════════════
   ADEXPERT / InfinityHome — Backup
   01/06/2026 à 14:30:00
═════════════════════════════════════════════════════════

▶  Sauvegarde de la base de données MySQL
  ℹ  mysqldump de la base 'infinityhome_db' sur localhost:3306
  ✔  Base de données → database_20260601_143000.sql (2.4 Mo)

▶  Sauvegarde des fichiers Media
  ℹ  847 fichier(s) média sauvegardé(s)
  ✔  Media → media_20260601_143000.zip (156.2 Mo)

▶  Sauvegarde du code source
  ℹ  312 fichier(s) de code sauvegardé(s)
  ✔  Code source → code_20260601_143000.zip (1.8 Mo)

▶  Assemblage du fichier ZIP final
  ℹ    Ajout : database_20260601_143000.sql
  ℹ    Ajout : media_20260601_143000.zip
  ℹ    Ajout : code_20260601_143000.zip
  ℹ    Ajout : backup_meta.json
  ✔  ZIP créé → infinityhome_backup_20260601_143000.zip
  ✔  Taille finale : 158.7 Mo
  ✔  Emplacement   : /srv/infinityhome/backups/infinityhome_backup_20260601_143000.zip
  ───────────────────────────────────────────────────────
  ✅  Backup terminé avec succès !
```