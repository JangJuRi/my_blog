from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    password_confirm = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to="users/profile", blank=True)
    nickname = models.CharField(max_length=20)
    blog_title = models.CharField(max_length=20, blank=True)
    blog_introduce = models.CharField(max_length=40, blank=True)

class GuestBook(models.Model):
    target_user = models.ForeignKey(
        User, verbose_name="방명록 대상자", on_delete=models.CASCADE, related_name='target_user'
    )
    write_user = models.ForeignKey(
        User, verbose_name="방명록 작성자", on_delete=models.CASCADE, related_name='write_user'
    )
    content = models.CharField(max_length=60)
    registDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)