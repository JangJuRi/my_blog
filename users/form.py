from django import forms
from users.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "username",
            "password",
            "password_confirm",
            "email",
            "first_name",
            "last_name"
        }
        labels = {
            "username" : "아이디",
            "password" : "비밀번호",
            "password_confirm" : "비밀번호 확인",
            "email" : "이메일",
            "last_name" : "성",
            "first_name" : "이름"
        }
        widgets = {
            "username" : forms.TextInput(attrs={'class': 'form-control'}),
            "password" : forms.PasswordInput(attrs={'class': 'form-control'}),
            "password_confirm" : forms.PasswordInput(attrs={'class': 'form-control'}),
            "email" : forms.EmailInput(attrs={'class': 'form-control'}),
            "last_name" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '성'}),
            "first_name" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름'})
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