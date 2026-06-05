from django.urls import path
from . import views

urlpatterns = [
    # ── Liste / création des groupes ──────────────────────────────
    # appelé par admin:    /api/chat/groups/
    # appelé par prop/loc: /api/chat/  (alias)
    path('',              views.GroupChatListCreate.as_view()),   # /api/chat/
    path('groups/',       views.GroupChatListCreate.as_view()),   # /api/chat/groups/

    # ── Détail d'un groupe ────────────────────────────────────────
    path('<int:pk>/',          views.GroupChatDetail.as_view()),  # /api/chat/1/
    path('groups/<int:pk>/',   views.GroupChatDetail.as_view()),  # /api/chat/groups/1/

    # ── Messages d'un groupe ──────────────────────────────────────
    # GET  → lire les messages
    # POST → envoyer un message  (admin utilise /send/, prop/loc utilisent POST sur /messages/)
    path('<int:pk>/messages/',        views.group_messages_or_send),  # /api/chat/1/messages/
    path('groups/<int:pk>/messages/', views.group_messages_or_send),  # /api/chat/groups/1/messages/

    # ── Envoi explicite (admin) ───────────────────────────────────
    path('<int:pk>/send/',        views.send_message),            # /api/chat/1/send/
    path('groups/<int:pk>/send/', views.send_message),            # /api/chat/groups/1/send/

    # ── Hiérarchie propriétaire → immeubles → groupes ─────────────
    path('hierarchy/', views.hierarchy),                          # /api/chat/hierarchy/
]
