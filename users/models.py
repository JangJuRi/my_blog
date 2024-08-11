from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    password_confirm = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to="users/profile", blank=True)
    nickname = models.CharField(max_length=20)
    blog_title = models.CharField(max_length=20, blank=True)
    blog_introduce = models.CharField(max_length=40, blank=True)