import datetime

from django.shortcuts import render, redirect
from board.models import Board, User

def board_list(request):
    try:
        boards = Board.objects.filter(title__contains=request.POST.get('searchTitle')).order_by("-id")
    except:
        boards = Board.objects.all().order_by("-id")

    context = {
        "boards": boards
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

def board_save(request):
    title = request.POST["title"]
    subTitle = request.POST["subTitle"]
    content = request.POST["content"]

    try:
        boardId = request.POST["boardId"]
        Board.objects.filter(id=boardId).update(
            title=title,
            subTitle=subTitle,
            content=content,
        )

        return redirect(f"/board/{boardId}")
    except:
        user = User.objects.get(id=1)
        board = Board.objects.create(
            title=title,
            subTitle=subTitle,
            content=content,
            user=user
        )

        return redirect(f"/board/{board.id}")