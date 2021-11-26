import django.forms
from django import forms
from .models import Question, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : 'Content'
        }

