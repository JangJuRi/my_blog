from django.urls import path
from users.views import login_page, logout_view, signup_page, my_page, modify_profile_image, modify_profile, save_guest_book

app_name="users"

urlpatterns = [

    path('login', login_page, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup_page, name="signup"),
    path('mypage/<str:username>', my_page, name="mypage"),
    path('profile-image/modify', modify_profile_image, name="modify_profile_image"),
    path('profile/modify', modify_profile, name="modify_profile"),
    path('guest_book/save', save_guest_book, name="save_guest_book"),
]