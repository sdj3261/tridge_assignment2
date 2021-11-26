from django.contrib import admin
from .models import Choice, Question, Comment

@admin.register(Question) #Wrapping
class QuestionAdmin(admin.ModelAdmin) :
    list_display = ['id','question_text','pub_date','is_public']
    search_fields = ['question_text']
@admin.register(Choice) #Wrapping
class ChoiceAdmin(admin.ModelAdmin) :
    list_display = ['question', 'choice_text', 'votes']
    search_fields = ['choice_text']

admin.site.register(Comment)

from django.contrib import admin
from . import models






