import jwt
import json

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from secret import SECRET
from members.models import User
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOnly(BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        access_token = request.headers.get('Authorization', None)
        payload = jwt.decode(access_token, SECRET)
        user = User.objects.get(id=payload['id'])
        if user.role == 'ADMIN':
            return True
        elif request.method in SAFE_METHODS:
            return True
        return False
