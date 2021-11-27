from datetime import datetime

from django.contrib import admin

from .models import Choice, Question, Comment


@admin.register(Question)  # Wrapping
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date','closed_at']
    search_fields = ['question_text']


@admin.register(Choice)  # Wrapping
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes', 'approved']
    search_fields = ['choice_text']

    def approve_posts(modeladmin, request, queryset):
        queryset.update(approved=True)

    def reject_posts(modeladmin, request, queryset):
        queryset.update(approved=False)

    approve_posts.short_description = "Approve selected posts"
    reject_posts.short_description = "Reject selected posts"
    actions = [approve_posts,reject_posts]


admin.site.register(Comment)

from django.contrib import admin
from . import models
