import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.conf import settings


class SessionTimeoutMiddleware:
    """
    Déconnecte automatiquement l'utilisateur après SESSION_COOKIE_AGE
    secondes d'inactivité (défaut : 300s = 5 minutes).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now()

            if last_activity:
                last_activity_time = datetime.datetime.fromisoformat(last_activity)

                # S'assurer que le datetime est timezone-aware
                if timezone.is_naive(last_activity_time):
                    last_activity_time = timezone.make_aware(last_activity_time)

                elapsed = (now - last_activity_time).total_seconds()
                timeout = getattr(settings, 'SESSION_COOKIE_AGE', 300)

                if elapsed > timeout:
                    # Vider la session et rediriger vers la page de login
                    request.session.flush()
                    login_url = getattr(settings, 'LOGIN_URL', '/login/')
                    return redirect(f"{login_url}?next={request.path}&timeout=1")

            # Mettre à jour le timestamp à chaque requête active
            request.session['last_activity'] = now.isoformat()

        return self.get_response(request)