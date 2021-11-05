import jwt
from rest_framework import authentication

from members.models import User
from secret import SECRET


class FreshcodeAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        access_token = request.headers.get('Authorization')
        if access_token:
            access_token = access_token[len("Bearer "):]
            payload = jwt.decode(access_token, SECRET, algorithms=["HS256"])
            userid = payload['id']
            user = User.objects.get(id=userid)
            return user, None
        return None
