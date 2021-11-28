import datetime

import django
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    closed_at = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=3))

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Comment(models.Model):
    # 1:N 구조 (Question 하나에 여러개의 댓글 매칭)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.content


class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField('Re', max_length=200)
    create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.content
