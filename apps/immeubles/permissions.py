# permissions.py  (créer ce fichier)
from rest_framework.permissions import BasePermission

class IsAdminOrGestionnaire(BasePermission):
    def has_permission(self, request, view):
        role = getattr(request.user, 'role', None)
        return request.user.is_authenticated and role in ('admin', 'gestionnaire')