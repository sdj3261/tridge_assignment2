import django.forms
from django import forms
from .models import Question, Comment, ReComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RecommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', 'comment')
        labels = {'content':'content', 'comment' :'comment'}
