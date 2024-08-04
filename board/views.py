import datetime

from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from board.form import AddBoardForm
from board.models import Board
from users.models import User

def board_list(request):
    search_title = request.GET.get('searchTitle')
    page_count = 3

    if search_title is not None:
        boards = Board.objects.filter(title__contains=search_title).order_by("-id")
    else:
        boards = Board.objects.all().order_by("-id")

    paginator = Paginator(boards, page_count)
    page = request.GET.get('page', 1)
    paginated_boards = paginator.get_page(page)

    context = {
        "boards": paginated_boards
    }

    return render(request, "index.html", context)

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)

    context = {
        "board": board
    }
    return render(request, "detail.html", context)

def board_write(request):
    try:
        board = Board.objects.get(id=request.POST["boardId"])
        context = {
            "board": board
        }

        return render(request, "write.html", context)

    except:
        return render(request, "write.html")

def save_board(request):
    form = AddBoardForm(request.POST, request.FILES)

    if form.is_valid():
        title = form.cleaned_data["title"]
        subTitle = form.cleaned_data["subTitle"]
        content = form.cleaned_data["content"]
        thumbnail_image = form.cleaned_data["thumbnail_image"]

        try:
            boardId = request.POST["boardId"]
            Board.objects.filter(id=boardId).update(
                title=title,
                subTitle=subTitle,
                content=content,
                thumbnail_image=thumbnail_image,
                modifyDate=timezone.now()
            )

            return redirect(f"/board/{boardId}")
        except:
            board = Board.objects.create(
                title=title,
                subTitle=subTitle,
                content=content,
                thumbnail_image=thumbnail_image,
                user=request.user
            )

            return redirect(f"/board/{board.id}")

def remove_board(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete();

    return redirect("/")