"""
╔══════════════════════════════════════════════════════════════╗
║          ADEXPERT / InfinityHome — Système de Backup         ║
║                                                              ║
║  Usage:                                                      ║
║    python manage.py backup                  → Backup complet ║
║    python manage.py backup --db-only        → BDD seulement  ║
║    python manage.py backup --media-only     → Media seulment ║
║    python manage.py backup --list           → Lister backups  ║
║    python manage.py backup --restore <nom>  → Restaurer       ║
║    python manage.py backup --clean --keep 5 → Garder 5 dern. ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import shutil
import zipfile
import json
import subprocess
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings


# ─── Couleurs terminal ─────────────────────────────────────────
class C:
    RESET  = '\033[0m'
    BOLD   = '\033[1m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    RED    = '\033[91m'
    CYAN   = '\033[96m'
    BLUE   = '\033[94m'
    GREY   = '\033[90m'

def ok(msg):    print(f"  {C.GREEN}✔{C.RESET}  {msg}")
def info(msg):  print(f"  {C.CYAN}ℹ{C.RESET}  {msg}")
def warn(msg):  print(f"  {C.YELLOW}⚠{C.RESET}  {msg}")
def err(msg):   print(f"  {C.RED}✘{C.RESET}  {msg}")
def step(msg):  print(f"\n{C.BOLD}{C.BLUE}▶  {msg}{C.RESET}")
def sep():      print(f"  {C.GREY}{'─'*55}{C.RESET}")


class Command(BaseCommand):
    help = 'Backup complet du projet InfinityHome (BDD MySQL + Media + Code)'

    def add_arguments(self, parser):
        parser.add_argument('--db-only',    action='store_true', help='Backup base de données uniquement')
        parser.add_argument('--media-only', action='store_true', help='Backup fichiers media uniquement')
        parser.add_argument('--code-only',  action='store_true', help='Backup code source uniquement')
        parser.add_argument('--list',       action='store_true', help='Lister les backups existants')
        parser.add_argument('--restore',    type=str,            help='Restaurer un backup (nom du fichier)')
        parser.add_argument('--clean',      action='store_true', help='Supprimer les anciens backups')
        parser.add_argument('--keep',       type=int, default=10, help='Nombre de backups à conserver (défaut: 10)')
        parser.add_argument('--output',     type=str,            help='Dossier de sortie personnalisé')
        
    def handle(self, *args, **options):
        
      
        # ── Dossier de backup ──────────────────────────────────
        base_dir = Path(settings.BASE_DIR)
        if options['output']:
            backup_root = Path(options['output'])
        else:
            backup_root = base_dir / 'backups'

        backup_root.mkdir(parents=True, exist_ok=True)

        # ── Router vers l'action demandée ──────────────────────
        if options['list']:
            self._list_backups(backup_root)
            return

        if options['restore']:
            self._restore_backup(backup_root, options['restore'], base_dir)
            return

        if options['clean']:
            self._clean_backups(backup_root, options['keep'])
            return

        # ── Lancement du backup ────────────────────────────────
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        date_fmt  = datetime.now().strftime('%d/%m/%Y à %H:%M:%S')

        print(f"\n{C.BOLD}{C.CYAN}{'═'*57}")
        print(f"   ADEXPERT / InfinityHome — Backup")
        print(f"   {date_fmt}")
        print(f"{'═'*57}{C.RESET}")

        results = {}

        # Déterminer ce qu'on sauvegarde
        do_db    = options['db_only'] or (not options['media_only'] and not options['code_only'])
        do_media = options['media_only'] or (not options['db_only'] and not options['code_only'])
        do_code  = options['code_only'] or (not options['db_only'] and not options['media_only'])

        # Dossier temporaire
        tmp_dir = backup_root / f'tmp_{timestamp}'
        tmp_dir.mkdir(parents=True, exist_ok=True)

        try:
            # ── 1. Base de données MySQL ───────────────────────
            if do_db:
                step("Sauvegarde de la base de données MySQL")
                db_file = self._backup_database(tmp_dir, timestamp)
                if db_file:
                    results['database'] = str(db_file.name)
                    ok(f"Base de données → {db_file.name} ({self._size(db_file)})")
                else:
                    warn("Backup BDD ignoré (voir erreur ci-dessus)")

            # ── 2. Fichiers Media ──────────────────────────────
            if do_media:
                step("Sauvegarde des fichiers Media")
                media_file = self._backup_media(tmp_dir, timestamp, base_dir)
                if media_file:
                    results['media'] = str(media_file.name)
                    ok(f"Media → {media_file.name} ({self._size(media_file)})")
                else:
                    warn("Aucun dossier media trouvé — ignoré")

            # ── 3. Code source ─────────────────────────────────
            if do_code:
                step("Sauvegarde du code source")
                code_file = self._backup_code(tmp_dir, timestamp, base_dir)
                if code_file:
                    results['code'] = str(code_file.name)
                    ok(f"Code source → {code_file.name} ({self._size(code_file)})")

            # ── 4. Métadonnées ─────────────────────────────────
            meta = {
                'timestamp'   : timestamp,
                'date'        : date_fmt,
                'version'     : '1.0',
                'project'     : 'InfinityHome / ADEXPERT',
                'contenu'     : results,
                'db_engine'   : settings.DATABASES.get('default', {}).get('ENGINE', '—'),
                'db_name'     : settings.DATABASES.get('default', {}).get('NAME', '—'),
                'python'      : sys.version,
                'django'      : self._django_version(),
            }
            meta_file = tmp_dir / 'backup_meta.json'
            meta_file.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding='utf-8')
            results['meta'] = 'backup_meta.json'

            # ── 5. Assembler le ZIP final ──────────────────────
            step("Assemblage du fichier ZIP final")
            zip_name = f'infinityhome_backup_{timestamp}.zip'
            zip_path = backup_root / zip_name

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
                for f in tmp_dir.iterdir():
                    zf.write(f, f.name)
                    info(f"  Ajout : {f.name}")

            ok(f"ZIP créé → {zip_name}")
            ok(f"Taille finale : {self._size(zip_path)}")
            ok(f"Emplacement   : {zip_path}")

        finally:
            # Nettoyer le dossier temporaire
            shutil.rmtree(tmp_dir, ignore_errors=True)

        # ── Résumé final ───────────────────────────────────────
        sep()
        print(f"\n{C.BOLD}{C.GREEN}  ✅  Backup terminé avec succès !{C.RESET}")
        print(f"  {C.GREY}Fichier : {zip_path}{C.RESET}\n")

        # Nettoyage automatique si > 15 backups
        existing = sorted(backup_root.glob('infinityhome_backup_*.zip'))
        if len(existing) > 15:
            warn(f"{len(existing)} backups détectés. Pensez à lancer --clean --keep 10")

    # ════════════════════════════════════════════════════════════
    #  BACKUP BASE DE DONNÉES MYSQL
    # ════════════════════════════════════════════════════════════
    def _backup_database(self, tmp_dir, timestamp):
        db = settings.DATABASES.get('default', {})
        engine = db.get('ENGINE', '')

        if 'mysql' not in engine:
            warn(f"Moteur détecté : {engine} — utilisation de dumpdata Django")
            return self._backup_db_django(tmp_dir, timestamp)

        # Paramètres MySQL
        db_name = db.get('NAME', '')
        db_user = db.get('USER', '')
        db_pass = db.get('PASSWORD', '')
        db_host = db.get('HOST', 'localhost')
        db_port = str(db.get('PORT', '3306'))

        sql_file = tmp_dir / f'database_{timestamp}.sql'

        # Construire la commande mysqldump
        cmd = ['mysqldump', '--single-transaction', '--routines', '--triggers',
               f'--host={db_host}', f'--port={db_port}',
               f'--user={db_user}', f'--password={db_pass}',
               db_name]

        try:
            info(f"mysqldump de la base '{db_name}' sur {db_host}:{db_port}")
            with open(sql_file, 'w', encoding='utf-8') as f:
                result = subprocess.run(
                    cmd, stdout=f, stderr=subprocess.PIPE,
                    text=True, timeout=300
                )
            if result.returncode != 0:
                err(f"mysqldump error: {result.stderr[:300]}")
                # Fallback sur dumpdata Django
                warn("Fallback sur dumpdata Django...")
                sql_file.unlink(missing_ok=True)
                return self._backup_db_django(tmp_dir, timestamp)
            return sql_file

        except FileNotFoundError:
            err("mysqldump non trouvé. Vérifiez que MySQL client est installé.")
            warn("Fallback sur dumpdata Django...")
            return self._backup_db_django(tmp_dir, timestamp)
        except subprocess.TimeoutExpired:
            err("Timeout mysqldump (300s). Base de données trop volumineuse ?")
            return None

    def _backup_db_django(self, tmp_dir, timestamp):
        """Fallback : utilise le dumpdata de Django (JSON)"""
        json_file = tmp_dir / f'database_{timestamp}_django.json'
        try:
            from django.core.management import call_command
            import io
            buf = io.StringIO()
            call_command('dumpdata', '--indent', '2',
                         '--exclude', 'contenttypes',
                         '--exclude', 'auth.permission',
                         stdout=buf)
            json_file.write_text(buf.getvalue(), encoding='utf-8')
            info("Backup via dumpdata Django (JSON)")
            return json_file
        except Exception as e:
            err(f"dumpdata échoué : {e}")
            return None

    # ════════════════════════════════════════════════════════════
    #  BACKUP MEDIA
    # ════════════════════════════════════════════════════════════
    def _backup_media(self, tmp_dir, timestamp, base_dir):
        media_root = getattr(settings, 'MEDIA_ROOT', None)
        if not media_root:
            media_root = base_dir / 'media'

        media_path = Path(media_root)
        if not media_path.exists() or not any(media_path.iterdir()):
            return None

        media_zip = tmp_dir / f'media_{timestamp}.zip'
        nb_files = 0

        with zipfile.ZipFile(media_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=4) as zf:
            for f in media_path.rglob('*'):
                if f.is_file():
                    arcname = f.relative_to(media_path.parent)
                    zf.write(f, arcname)
                    nb_files += 1

        info(f"{nb_files} fichier(s) média sauvegardé(s)")
        return media_zip

    # ════════════════════════════════════════════════════════════
    #  BACKUP CODE SOURCE
    # ════════════════════════════════════════════════════════════
    def _backup_code(self, tmp_dir, timestamp, base_dir):
        code_zip = tmp_dir / f'code_{timestamp}.zip'

        # Patterns à exclure
        EXCLUDE = {
            '__pycache__', '.git', 'node_modules', 'venv', 'env',
            '.venv', 'backups', 'tmp', '.idea', '.vscode',
            '*.pyc', '*.pyo', '*.log', '*.sqlite3',
            'media', 'staticfiles', 'static_collected',
        }

        def should_exclude(path: Path) -> bool:
            for part in path.parts:
                if part in EXCLUDE:
                    return True
                if part.endswith('.pyc') or part.endswith('.log'):
                    return True
            return False

        nb_files = 0
        with zipfile.ZipFile(code_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
            for f in base_dir.rglob('*'):
                if f.is_file() and not should_exclude(f.relative_to(base_dir)):
                    try:
                        arcname = f'code/{f.relative_to(base_dir)}'
                        zf.write(f, arcname)
                        nb_files += 1
                    except (PermissionError, OSError):
                        pass

        info(f"{nb_files} fichier(s) de code sauvegardé(s)")
        return code_zip

    # ════════════════════════════════════════════════════════════
    #  LISTER LES BACKUPS
    # ════════════════════════════════════════════════════════════
    def _list_backups(self, backup_root):
        backups = sorted(backup_root.glob('infinityhome_backup_*.zip'), reverse=True)

        print(f"\n{C.BOLD}{C.CYAN}  Backups disponibles ({len(backups)}){C.RESET}")
        sep()

        if not backups:
            warn("Aucun backup trouvé dans " + str(backup_root))
            return

        total_size = 0
        for i, b in enumerate(backups, 1):
            size = b.stat().st_size
            total_size += size
            # Extraire la date du nom
            try:
                ts = b.stem.replace('infinityhome_backup_', '')
                dt = datetime.strptime(ts, '%Y%m%d_%H%M%S')
                date_str = dt.strftime('%d/%m/%Y %H:%M:%S')
            except:
                date_str = '—'

            age = (datetime.now() - datetime.fromtimestamp(b.stat().st_mtime))
            age_str = f"{age.days}j" if age.days > 0 else f"{age.seconds//3600}h"

            print(f"  {C.GREY}{i:2}.{C.RESET} {C.BOLD}{b.name}{C.RESET}")
            print(f"       📅 {date_str}  |  💾 {self._fmt_size(size)}  |  🕐 il y a {age_str}")

        sep()
        print(f"  {C.GREY}Total : {self._fmt_size(total_size)}{C.RESET}")
        print(f"  {C.GREY}Dossier : {backup_root}{C.RESET}\n")

    # ════════════════════════════════════════════════════════════
    #  NETTOYER LES ANCIENS BACKUPS
    # ════════════════════════════════════════════════════════════
    def _clean_backups(self, backup_root, keep):
        backups = sorted(backup_root.glob('infinityhome_backup_*.zip'), reverse=True)
        to_delete = backups[keep:]

        step(f"Nettoyage — conservation des {keep} derniers backups")

        if not to_delete:
            ok(f"Rien à supprimer ({len(backups)} backup(s) présent(s))")
            return

        freed = 0
        for b in to_delete:
            freed += b.stat().st_size
            b.unlink()
            ok(f"Supprimé : {b.name}")

        sep()
        ok(f"{len(to_delete)} backup(s) supprimé(s) — {self._fmt_size(freed)} libérés")

    # ════════════════════════════════════════════════════════════
    #  RESTAURER UN BACKUP
    # ════════════════════════════════════════════════════════════
    def _restore_backup(self, backup_root, backup_name, base_dir):
        # Trouver le fichier
        if not backup_name.endswith('.zip'):
            backup_name += '.zip'

        zip_path = backup_root / backup_name
        if not zip_path.exists():
            # Chercher par correspondance partielle
            matches = list(backup_root.glob(f'*{backup_name}*'))
            if matches:
                zip_path = matches[0]
            else:
                err(f"Backup introuvable : {backup_name}")
                info(f"Utilisez --list pour voir les backups disponibles")
                return

        step(f"Restauration de : {zip_path.name}")
        warn("⚠️  Cette opération va écraser la base de données et les fichiers media !")
        confirm = input(f"\n  {C.YELLOW}Confirmez avec 'OUI' pour continuer : {C.RESET}")

        if confirm.strip() != 'OUI':
            info("Restauration annulée.")
            return

        # Extraire dans un dossier temp
        tmp_dir = backup_root / 'restore_tmp'
        tmp_dir.mkdir(exist_ok=True)

        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(tmp_dir)

            # Lire les métadonnées
            meta_file = tmp_dir / 'backup_meta.json'
            if meta_file.exists():
                meta = json.loads(meta_file.read_text(encoding='utf-8'))
                info(f"Backup du : {meta.get('date', '—')}")
                info(f"Contenu   : {list(meta.get('contenu', {}).keys())}")

            # Restaurer la BDD
            sql_files  = list(tmp_dir.glob('database_*.sql'))
            json_files = list(tmp_dir.glob('database_*.json'))

            if sql_files:
                step("Restauration MySQL")
                self._restore_mysql(sql_files[0])
            elif json_files:
                step("Restauration Django (JSON)")
                self._restore_django(json_files[0])

            # Restaurer les media
            media_zips = list(tmp_dir.glob('media_*.zip'))
            if media_zips:
                step("Restauration des fichiers Media")
                media_root = Path(getattr(settings, 'MEDIA_ROOT', base_dir / 'media'))
                with zipfile.ZipFile(media_zips[0], 'r') as zf:
                    zf.extractall(media_root.parent)
                ok(f"Media restaurés dans {media_root}")

            ok("Restauration terminée avec succès !")

        except Exception as e:
            err(f"Erreur lors de la restauration : {e}")
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    def _restore_mysql(self, sql_file):
        db = settings.DATABASES.get('default', {})
        cmd = ['mysql',
               f"--host={db.get('HOST','localhost')}",
               f"--port={str(db.get('PORT','3306'))}",
               f"--user={db.get('USER','')}",
               f"--password={db.get('PASSWORD','')}",
               db.get('NAME','')]
        try:
            with open(sql_file, 'r', encoding='utf-8') as f:
                result = subprocess.run(cmd, stdin=f, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                ok(f"Base de données restaurée depuis {sql_file.name}")
            else:
                err(f"Erreur MySQL : {result.stderr[:200]}")
        except Exception as e:
            err(f"Restauration MySQL échouée : {e}")

    def _restore_django(self, json_file):
        try:
            from django.core.management import call_command
            call_command('loaddata', str(json_file))
            ok(f"Données restaurées depuis {json_file.name}")
        except Exception as e:
            err(f"loaddata échoué : {e}")

    # ════════════════════════════════════════════════════════════
    #  UTILITAIRES
    # ════════════════════════════════════════════════════════════
    def _size(self, path: Path) -> str:
        return self._fmt_size(path.stat().st_size)

    def _fmt_size(self, size: int) -> str:
        for unit in ['o', 'Ko', 'Mo', 'Go']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} To"

    def _django_version(self) -> str:
        try:
            import django
            return django.get_version()
        except:
            return '—'