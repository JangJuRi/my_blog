from django.urls import path
from board.views import board_detail, board_write, save_board, remove_board, save_comment, remove_comment

app_name="board"

urlpatterns = [
    path('<int:board_id>/', board_detail, name="board_detail"),
    path('write/', board_write, name="board_write"),
    path('save/', save_board, name="save_board"),
    path('remove/<int:board_id>/', remove_board, name="remove_board"),
    path('comment/save', save_comment, name="save_comment"),
    path('comment/remove', remove_comment, name="remove_comment")
]