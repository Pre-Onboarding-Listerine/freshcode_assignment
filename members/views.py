from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer
from members import serializers

# Create your views here.
class SignupView(CreateAPIView):
	model = get_user_model()
	serializer_class = SignupSerializer
