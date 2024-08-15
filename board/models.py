from django.db import models
from ckeditor.fields import RichTextField

from users.models import User

class Board(models.Model):
    title = models.CharField(max_length=40)
    subTitle = models.CharField(max_length=60, null=True)
    content = RichTextField(max_length=4000)
    views = models.IntegerField(default=0)
    thumbnail_image = models.ImageField(upload_to="board/thumbnail", null=True, blank=True)
    registDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey (
        User, verbose_name="등록자", on_delete=models.CASCADE
    )

class Comment(models.Model):
    content = models.CharField(max_length=4000)
    root_yn = models.CharField(max_length=1, default="Y")
    regist_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    board = models.ForeignKey (
        Board, verbose_name="게시글", on_delete=models.CASCADE
    )
    user = models.ForeignKey (
        User, verbose_name="등록자", on_delete=models.CASCADE
    )
    upper_comment = models.ForeignKey (
        'self', verbose_name="답글", on_delete=models.CASCADE, null=True, blank=True
    )
