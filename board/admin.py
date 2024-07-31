from django.contrib import admin
from board.models import Board, User

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass