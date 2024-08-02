from django import forms
from users.models import User
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "accountId",
            "password"
        }
        labels = {
            "accountId" : "아이디",
            "password" : "비밀번호"
        }
        widgets = {
            "accountId" : forms.TextInput(attrs={'class': 'form-control'}),
            "password" : forms.PasswordInput(attrs={'class': 'form-control'})
        }