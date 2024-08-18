from django import forms
from users.models import User, GuestBook


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "username",
            "password",
            "password_confirm",
            "email",
            "first_name",
            "last_name",
            "nickname"
        }
        widgets = {
            "username" : forms.TextInput(attrs={'class': 'form-control'}),
            "password" : forms.PasswordInput(attrs={'class': 'form-control'}),
            "password_confirm" : forms.PasswordInput(attrs={'class': 'form-control'}),
            "email" : forms.EmailInput(attrs={'class': 'form-control'}),
            "last_name" : forms.TextInput(attrs={'class': 'form-control'}),
            "first_name" : forms.TextInput(attrs={'class': 'form-control'}),
            "nickname" : forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "username",
            "password",
        }
        labels = {
            "username" : "아이디",
            "password" : "비밀번호",
        }
        widgets = {
            "username" : forms.TextInput(attrs={'class': 'form-control'}),
            "password" : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "nickname",
            "blog_title",
            "blog_introduce",
        }
        widgets = {
            "nickname": forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': '닉네임을 입력해주세요.'}),
            "blog_title": forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': '블로그명을 입력해주세요.'}),
            "blog_introduce": forms.TextInput(attrs={'class': 'form-control', 'placeholder': '블로그 소개를 입력해주세요.'}),
        }

class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = {
            "content"
        }
        widgets = {
            "content": forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': '방명록을 입력해주세요.'}),
        }