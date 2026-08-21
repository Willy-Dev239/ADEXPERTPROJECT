import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.conf import settings


class SessionTimeoutMiddleware:
    """
    Déconnecte automatiquement l'utilisateur après SESSION_COOKIE_AGE
    secondes d'inactivité (défaut : 300s = 5 minutes).
    Ne s'applique qu'aux requêtes web classiques (session cookie),
    jamais aux requêtes API authentifiées par Token.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ✅ Ne jamais toucher aux requêtes API (Token auth) — laisser DRF gérer ça lui-même
        if request.path.startswith('/api/'):
            return self.get_response(request)

        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now()

            if last_activity:
                last_activity_time = datetime.datetime.fromisoformat(last_activity)

                if timezone.is_naive(last_activity_time):
                    last_activity_time = timezone.make_aware(last_activity_time)

                elapsed = (now - last_activity_time).total_seconds()
                timeout = getattr(settings, 'SESSION_COOKIE_AGE', 300)

                if elapsed > timeout:
                    request.session.flush()
                    login_url = getattr(settings, 'LOGIN_URL', '/login/')
                    return redirect(f"{login_url}?next={request.path}&timeout=1")

            request.session['last_activity'] = now.isoformat()

        return self.get_response(request)