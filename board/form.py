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
        labels = {
            "title": "타이틀",
            "subTitle": "서브타이틀",
            "content": "내용",
        }