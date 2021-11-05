from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True, max_length=120)
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=12)