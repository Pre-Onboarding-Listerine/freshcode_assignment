from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    def create(self, validated_data):
        self.password = validated_data["password"]
        new_salt = bcrypt.gensalt(12)
        hashed_password = bcrypt.hashpw(validated_data["password"].encode('utf-8'), new_salt)
        self.password = hashed_password
        user = User.objects.create(email=validated_data["email"], password=hashed_password)
        return user

    class Meta:
        model = User
        fields = ["email", "password"]
