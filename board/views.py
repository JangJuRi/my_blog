from django.shortcuts import render, redirect
from board.models import Board, User

def board_list(request):
    try:
        boards = Board.objects.filter(title__contains=request.POST.get('searchTitle'))
    except:
        boards = Board.objects.all()

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
    if request.method == 'POST':
        title = request.POST["title"]
        subTitle = request.POST["subTitle"]
        content = request.POST["content"]
        user = User.objects.get(id=1)

        board = Board.objects.create(
            title=title,
            subTitle=subTitle,
            content=content,
            user=user
        )

        return redirect(f"/board/{board.id}")
    else:
        return render(request, "write.html")
