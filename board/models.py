from django.db import models

from users.models import User

class Board(models.Model):
    title = models.CharField(max_length=20)
    subTitle = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=4000)
    views = models.IntegerField(default=0)
    thumbnail_image = models.ImageField(upload_to="board/thumbnail", null=True, blank=True)
    registDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey (
        User, verbose_name="등록자", on_delete=models.CASCADE
    )
