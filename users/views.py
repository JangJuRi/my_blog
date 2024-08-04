from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.form import LoginForm, SignUpForm
from users.models import User

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            print("계정정보 일치X")


        return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")

def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirm = form.cleaned_data["password_confirm"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            nickname = form.cleaned_data["nickname"]

            if password != password_confirm:
                form.add_error("password_confirm", "비밀번호가 일치하지 않습니다.")

            if User.objects.filter(username=username).exists():
                form.add_error("username", "이미 존재하는 아이디입니다.")

            if form.errors:
                return render(request, 'signup.html', {'form': form})

            else:
                User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    nickname=nickname
                )
                return redirect("/login")
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})