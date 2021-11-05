import bcrypt
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
import jwt
from .models import User
from .serializers import UserSerializer
from secret import SECRET


# Create your views here.
class SignupView(CreateAPIView):
	model = User
	serializer_class = UserSerializer


class SigninView(APIView):
	def post(self, request, format=None):
		user = User.objects.get(email=request.data["email"])
		if not user:
			return Response(" 존재하지 않는 이메일 ", status=status.HTTP_404_NOT_FOUND)
		if not bcrypt.checkpw(request.data["password"].encode('utf-8'), user.password.encode('utf-8')):
			return Response(" 유효하지 않은 비밀번호 ", status=status.HTTP_401_UNAUTHORIZED)
		token = "Bearer " + jwt.encode({'id': user.id }, SECRET)
		return Response(token, status=status.HTTP_200_OK)
