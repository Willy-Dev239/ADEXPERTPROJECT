# A — Gestion Locative

Système complet de gestion locative basé sur Django REST Framework.




1. Créer la base de données MySQL

CREATE DATABASE adexpert_recouvrement_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'adexpert'@'localhost' IDENTIFIED BY 'adexpert2121';
GRANT ALL PRIVILEGES ON adexpert_recouvrement_db.* TO 'adexpert'@'localhost';
FLUSH PRIVILEGES;



2. Configurer infinityhome/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adexpert_recouvrement_db',
        'USER': 'adexpert',
        'PASSWORD': 'adexpert2121',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



## Installation rapide

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Accès

- **Admin/Gestionnaire** → http://localhost:8000/
- **Propriétaire** → http://localhost:8000/proprietaire/
- **Locataire** → http://localhost:8000/locataire/
- **Connexion** → http://localhost:8000/login/
- **API** → http://localhost:8000/api/

## Créer un utilisateur propriétaire

```bash
python manage.py shell
>>> from apps.auth_app.models import User
>>> from apps.proprietaires.models import Proprietaire
>>> p = Proprietaire.objects.create(nom="NDAYISHIMIYE Jean")
>>> u = User.objects.create_user('jean.prop', password='pass1234', role='proprietaire')
>>> u.proprietaire_profile = p; u.save()
```

## 9 Fonctionnalités implémentées

1. **Dashboard Locataire** — connexion + upload bordereau de paiement (photo)
2. **Quittance compacte A5** — signature unique admin/gestionnaire, impression optimisée
3. **Historique locataire** — tous les loyers payés/restants avec détail des paiements
4. **Dashboard Propriétaire** — vue isolée : ses locaux, locataires, loyers, charges uniquement
5. **Group Chat par immeuble** — sélection propriétaire → immeuble → groupe, polling temps réel
6. **Provinces du Burundi** — Bujumbura, Gitega, Burunga, Butanyerera, Buhumuza + communes cascadées
7. **Contrats Société étendus** — services loyers impayés, assurances, judiciaire, impôts, clients, touristique
8. **Notifications de paiement** — alertes automatiques aux locataires après paiement/bordereau
9. **CSRF Token** — endpoint /api/auth/csrf/ + intégration login sécurisé

## Structure des apps

```
apps/
├── auth_app/          — Utilisateurs (5 rôles)
├── proprietaires/     — Propriétaires
├── immeubles/         — Immeubles + provinces Burundi
├── locaux/            — Locaux (appartements, bureaux, etc.)
├── locataires/        — Locataires + upload bordereaux
├── contrats/          — Contrats location + contrats société
├── loyers/            — Loyers, paiements, quittances
├── charges/           — Charges et frais
├── dashboard/         — Dashboard + portefeuille
├── chat/              — Group chat par immeuble
└── notifications/     — Notifications locataires
```

## Variables d'environnement (production)

```env
SECRET_KEY=votre-cle-secrete
DEBUG=False
ALLOWED_HOSTS=votre-domaine.com
DATABASE_URL=postgresql://...
REDIS_URL=redis://localhost:6379/0
```
