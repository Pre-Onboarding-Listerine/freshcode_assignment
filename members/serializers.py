from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User



class SignupSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		user = User.objects.create(email=validated_data["email"])
		user.name = (validated_data["email"])
		user.password = make_password(validated_data["password"])
		user.save()
		return user
		
	class Meta:
		model = User
		fields = ["email", "password"]