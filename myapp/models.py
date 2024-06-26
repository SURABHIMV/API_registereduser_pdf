from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class New_user(AbstractUser):
    username =models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    image=models.ImageField(upload_to="", null=True, blank=True)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS= []