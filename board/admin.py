from django.contrib import admin
from board.models import Board, User, Comment


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    pass