from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
import jwt
from .models import User
from .serializers import UserSerializer


# Create your views here.
class SignupView(CreateAPIView):
	model = User
	serializer_class = UserSerializer


class SigninView(APIView):
	def post(self, request, format=None):
		user = User.objects.get(email=request.data["email"])
		if not user:
			return Response(" 존재하지 않는 이메일 ", status=status.HTTP_400_BAD_REQUEST)
		print(request.data["password"], "=====================", user.password)
		if not check_password(request.data["password"], user.password):
			return Response(" 유효하지 않은 비밀번호 ", status=status.HTTP_400_BAD_REQUEST)
		token = jwt.encode({'id': user.id }, "freshcode")
		return Response(token, status=status.HTTP_200_OK)