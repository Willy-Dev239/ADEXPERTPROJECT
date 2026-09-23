import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout


class SessionTimeoutMiddleware:
    """
    Déconnecte automatiquement l'utilisateur après SESSION_COOKIE_AGE
    secondes d'inactivité (défaut : 300s = 5 minutes).

    Ne s'applique qu'aux requêtes web classiques (session cookie).
    Les requêtes API (Token) sont ignorées — voir TokenExpiryMiddleware.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ne jamais toucher aux requêtes API (Token auth)
        if request.path.startswith('/api/'):
            return self.get_response(request)

        #  Ne pas déconnecter sur la page de login elle-même
        login_url = getattr(settings, 'LOGIN_URL', '/login/')
        if request.path.startswith(login_url):
            return self.get_response(request)

        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now()
            timeout = getattr(settings, 'SESSION_COOKIE_AGE', 300)

            if last_activity:
                last_activity_time = datetime.datetime.fromisoformat(last_activity)

                # Force le fuseau horaire si naïf
                if timezone.is_naive(last_activity_time):
                    last_activity_time = timezone.make_aware(
                        last_activity_time, timezone.get_current_timezone()
                    )

                elapsed = (now - last_activity_time).total_seconds()

                if elapsed > timeout:
                    # Déconnexion propre
                    logout(request)
                    request.session.flush()
                    return redirect(f"{login_url}?next={request.path}&timeout=1")

            #  Met à jour l'horodatage à CHAQUE requête
            request.session['last_activity'] = now.isoformat()
            request.session.modified = True

        return self.get_response(request)