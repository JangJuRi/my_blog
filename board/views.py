from django.shortcuts import render
from board.models import Board

def board_list(request):
    boards = Board.objects.all()

    context = {
        "boards": boards
    }

    return render(request, "index.html", context)

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)

    context =  {
        "board": board
    }
    return render(request, "detail.html", context)
