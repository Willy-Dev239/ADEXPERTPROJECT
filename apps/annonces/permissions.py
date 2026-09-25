from rest_framework.permissions import BasePermission


class PeutEcrire(BasePermission):
    """Admin, gestionnaire ou superuser."""

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.peut_ecrire)