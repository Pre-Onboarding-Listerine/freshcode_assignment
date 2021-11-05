from django.db import models
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True, max_length=120)
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=12)

    def get_model(self):
        return
