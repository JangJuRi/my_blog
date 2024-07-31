from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    subTitle = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=4000, null=True)
    views = models.IntegerField(default=0)
    registDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey (
        User, verbose_name="등록자", on_delete=models.CASCADE, null=True
    )
