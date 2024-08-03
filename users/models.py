from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    password_confirm = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="users/profile", blank=True)
