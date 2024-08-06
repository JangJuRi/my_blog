import datetime

from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from board.form import AddBoardForm
from board.models import Board, Comment
from users.models import User

def board_list(request):
    search_title = request.GET.get('searchTitle')
    page_count = 6

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
    comments = Comment.objects.filter(board=board).order_by("id")

    context = {
        "board": board,
        "comments": comments
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
    board_id = request.POST["boardId"]
    form = AddBoardForm(request.POST, request.FILES)

    if form.is_valid():
        title = form.cleaned_data["title"]
        subTitle = form.cleaned_data["subTitle"]
        content = form.cleaned_data["content"]
        thumbnail_image = form.cleaned_data["thumbnail_image"]

        if board_id:
            Board.objects.filter(id=board_id).update(
                title=title,
                subTitle=subTitle,
                content=content,
                modifyDate=timezone.now()
            )

            if thumbnail_image:
                board = Board.objects.get(id=board_id)
                board.thumbnail_image = thumbnail_image
                board.save()

            return redirect(f"/board/{board_id}")
        else:
            board = Board.objects.create(
                title=title,
                subTitle=subTitle,
                content=content,
                thumbnail_image=thumbnail_image,
                user=request.user
            )

            return redirect(f"/board/{board.id}")

    return redirect("/")

def remove_board(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()

    return redirect("/")

def save_comment(request):
    board_id = request.POST["boardId"]
    comment_id = request.POST.get("commentId", False)
    print("-------------------------------")
    print(comment_id)
    content = request.POST["content"]

    if comment_id:
        Comment.objects.filter(id=comment_id).update(
            content=content,
            modify_date=timezone.now()
        )

    else:
        Comment.objects.create (
            content=content,
            regist_date=timezone.now(),
            modify_date=timezone.now(),
            board=Board.objects.get(id=board_id),
            user=request.user
        )

    return redirect(f"/board/{board_id}")

def remove_comment(request):
    board_id = request.POST["boardId"]
    comment_id = request.POST.get("commentId")

    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect(f"/board/{board_id}")