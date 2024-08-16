import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from board.form import AddBoardForm
from board.models import Board, Comment

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
    is_exist = Board.objects.filter(id=board_id).exists()

    if is_exist:
        board = Board.objects.get(id=board_id)
        comments = Comment.objects.filter(board=board).order_by("upper_comment", "id")
        form = AddBoardForm(instance=board)

        # 조회수 연속 증가 방지 쿠키 세팅
        cookie = 'board_view_cookie_' + str(request.user.id) + '_' + str(board_id)

        if (cookie not in request.COOKIES):
            board.views = board.views + 1
            board.save()

            context = {
                "board": board,
                "comments": comments,
                "form": form
            }

            response = HttpResponse(render(request, 'detail.html', context))
            tomorrow = datetime.datetime.replace(datetime.datetime.now(), hour=23, minute=59, second=0)
            expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
            response.set_cookie(cookie, 'Y', expires=expires)

            return response

        else:
            context = {
                "board": board,
                "comments": comments,
                "form": form
            }

            return render(request, "detail.html", context)

    else:
        return render(request, "error.html", {"error_message":"존재하지 않는 게시글입니다."})

def board_write(request):
    board_id = request.POST.get("boardId", False)

    if board_id:
        board = Board.objects.get(id=board_id)
        form = AddBoardForm(instance=board)
        context = {
            "board": board,
            "form": form
        }

        return render(request, "write.html", context)

    else:
        form = AddBoardForm(data=request.POST)
        return render(request, "write.html", {"form": form})

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

            return redirect("board:board_detail", board_id)
        else:
            board = Board.objects.create(
                title=title,
                subTitle=subTitle,
                content=content,
                thumbnail_image=thumbnail_image,
                user=request.user
            )

            return redirect("board:board_detail", board.id)

    else:
        error_messages = []
        for field, errors in form.errors.items():
            if errors:
                label = form.fields[field].label
                error_messages.append(f"{label}: {errors[0]}")
                break

        board = {
            "title": request.POST["title"],
            "subTitle": request.POST["subTitle"],
            "content": request.POST["content"],
            "error_messages": error_messages,
        }

        context = {
            "board": board
        }

        return render(request, "write.html", context)

def remove_board(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()

    return redirect("/")

def save_comment(request):
    board_id = request.POST["boardId"]
    comment_id = request.POST.get("commentId", False)
    upper_comment_id = request.POST.get("upperCommentId", comment_id)
    content = request.POST["content"]

    if comment_id:
        Comment.objects.filter(id=comment_id).update(
            content=content,
            modify_date=timezone.now()
        )

    else:
        comment = Comment.objects.create (
            content=content,
            regist_date=timezone.now(),
            modify_date=timezone.now(),
            board=Board.objects.get(id=board_id),
            user=request.user
        )

        if comment_id != upper_comment_id:
            comment.root_yn = "N"
            comment.upper_comment = Comment.objects.get(id=upper_comment_id)
            comment.save()
        else:
            comment.upper_comment = comment
            comment.save()

    return redirect("board:board_detail", board_id)

def remove_comment(request):
    board_id = request.POST["boardId"]
    comment_id = request.POST.get("commentId")

    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect("board:board_detail", board_id)