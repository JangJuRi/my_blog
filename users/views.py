from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect

from board.models import Board, Comment
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
                return redirect("users:login")
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

def my_page(request, username):
    user = User.objects.get(username=username)
    boards = Board.objects.filter(user=user).order_by("-id")

    page_count = 6
    paginator = Paginator(boards, page_count)
    page = request.GET.get('page', 1)
    paginated_boards = paginator.get_page(page)

    context = {
        "user": user,
        "post_count": Board.objects.filter(user=user).aggregate(total_posts=Count('id'))['total_posts'],
        "comment_count": Comment.objects.filter(user=user).aggregate(total_comments=Count('id'))['total_comments'],
        "boards": paginated_boards
    }

    return render(request, 'mypage.html', context)