from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.form import LoginForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            accountId = form.cleaned_data["accountId"]
            password = form.cleaned_data["password"]

            user = authenticate(username=accountId, password=password)

            if user:
                login(request, user)
                return redirect("/")
            else:
                print("계정정보 일치X")
        else:
            print('에러')

        return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")