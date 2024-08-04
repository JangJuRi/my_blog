from django import forms

from board.models import Board

class AddBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = {
            "title",
            "subTitle",
            "content",
            "thumbnail_image"
        }