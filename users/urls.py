from django.urls import path
from users.views import login_page, logout_view, signup_page, my_page

app_name="users"

urlpatterns = [

    path('login', login_page, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup_page, name="signup"),
    path('mypage/<str:username>', my_page, name="mypage"),
]