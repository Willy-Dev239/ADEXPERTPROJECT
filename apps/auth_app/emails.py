from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def envoyer_code_verification(client_email, code, client_nom=""):
    salutation = f"Bonjour {client_nom}," if client_nom else "Bonjour,"
    texte = (
        f"{salutation}\n\n"
        f"Votre code de vérification : {code}\n"
        f"Il expire dans 10 minutes.\n\n"
        f"Si vous n'êtes pas à l'origine de cette demande, ignorez ce message."
    )
    html = f"""
    <div style="font-family:Arial,sans-serif;max-width:480px;margin:auto;padding:24px;border:1px solid #eee;border-radius:8px">
      <h2 style="color:#1a3c6e">ADEXPERT</h2>
      <p>{salutation}</p>
      <p>Votre code de vérification :</p>
      <p style="font-size:32px;font-weight:bold;letter-spacing:6px;color:#1a3c6e">{code}</p>
      <p style="color:#666">Il expire dans 10 minutes.</p>
      <p style="color:#999;font-size:12px">Si vous n'êtes pas à l'origine de cette demande, ignorez ce message.</p>
    </div>
    """
    msg = EmailMultiAlternatives(
        subject="ADEXPERT — Votre code de vérification",
        body=texte,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[client_email],
    )
    msg.attach_alternative(html, "text/html")
    msg.send(fail_silently=False)