from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsWritableOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(
            request.method in SAFE_METHODS or
            request.user.role.lower() == 'admin'
        )
