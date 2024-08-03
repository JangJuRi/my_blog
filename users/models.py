from django.db import models

class User(models.Model):
    accountId = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)