"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from board.views import board_list, board_detail, board_write, save_board, remove_board
from users.views import login_page, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board_list),
    path('board/<int:board_id>/', board_detail),
    path('board/write/', board_write),
    path('board/save/', save_board),
    path('board/remove/<int:board_id>/', remove_board),
    path('login/', login_page),
    path('logout/', logout_view)
]
