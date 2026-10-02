# A — Gestion Locative

## Installation

### Lancer le projet

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Contribuer au projet

Le dépôt est privé : l'accès doit être accordé par l'administrateur.

1. **Créer un compte GitHub** sur https://github.com/signup (si vous n'en avez pas déjà un).
2. **Envoyer votre nom d'utilisateur GitHub** à l'administrateur du projet et lui **demander l'accès** au dépôt.
3. **Accepter l'invitation** reçue par e-mail ou dans vos notifications GitHub.
4. **Cloner le dépôt** :

   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DEPOT>
   ```

5. **Créer une branche** pour votre travail (ne jamais travailler directement sur `main`) :

   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   ```

6. **Committer et pousser** vos modifications :

   ```bash
   git add .
   git commit -m "Description claire de la modification"
   git push origin feature/nom-de-la-fonctionnalite
   ```

7. **Ouvrir une Pull Request** vers `main` et attendre la validation de l'administrateur avant la fusion.

## Variables d'environnement (production)

```env
SECRET_KEY=votre-cle-secrete
DEBUG=False
ALLOWED_HOSTS=votre-domaine.com
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=3306
REDIS_URL=redis://localhost:6379/0
```
