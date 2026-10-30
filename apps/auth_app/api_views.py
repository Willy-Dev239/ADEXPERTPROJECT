import logging
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .emails import envoyer_code_verification
from .models import EmailVerification
from .serializers import RegisterSerializer

User = get_user_model()
log = logging.getLogger(__name__)
DELAI_RENVOI = timedelta(seconds=60)


class PublicAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]


def _user_en_attente(username):
    return User.objects.filter(
        username__iexact=(username or "").strip(),
        is_active=False,
        email_verification__isnull=False,
    ).select_related("email_verification").first()


def _emettre_et_envoyer(user):
    code = EmailVerification.issue(user)
    envoyer_code_verification(user.email, code, user.full_name)


class RegisterView(PublicAPIView):
    def post(self, request):
        ser = RegisterSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        try:
            _emettre_et_envoyer(user)
        except Exception:
            log.exception("Envoi du code impossible")
            user.delete()
            return Response({"detail": "Envoi de l'email impossible. Réessayez."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({"username": user.username, "email": user.email},
                        status=status.HTTP_201_CREATED)


class VerifyEmailView(PublicAPIView):
    def post(self, request):
        username = request.data.get("username")
        code = str(request.data.get("code", "")).strip()
        user = _user_en_attente(username)
        if not user:
            log.warning("verify-email: aucun compte en attente pour %r", username)
            return Response({"detail": "Code invalide ou expiré."}, status=400)

        ev = user.email_verification
        if ev.attempts >= EmailVerification.MAX_ATTEMPTS:
            return Response({"detail": "Trop de tentatives. Demandez un nouveau code."}, status=429)
        if not ev.verify_code(code):
            log.warning("verify-email: code refusé pour %s (expiré=%s)", user.username, ev.is_expired())
            return Response({"detail": "Code invalide ou expiré."}, status=400)

        user.is_active = True
        user.save(update_fields=["is_active"])
        ev.delete()
        return Response({"detail": "Compte vérifié."})


class ResendCodeView(PublicAPIView):
    def post(self, request):
        user = _user_en_attente(request.data.get("username"))
        if not user:
            return Response({"detail": "Demande invalide."}, status=400)

        if timezone.now() < user.email_verification.created_at + DELAI_RENVOI:
            return Response({"detail": "Patientez avant de renvoyer un code."}, status=429)

        try:
            _emettre_et_envoyer(user)
        except Exception:
            log.exception("Renvoi du code impossible")
            return Response({"detail": "Envoi de l'email impossible. Réessayez."}, status=503)
        return Response({"detail": "Code renvoyé."})