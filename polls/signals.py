import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Question, Choice


@receiver(post_save, sender=Choice)
def question_post_save(sender, **kwargs):
    question = kwargs['instance'].question
    question.is_public = False
    question.pub_date = timezone.now() + datetime.timedelta(days=1)
    question.save()


post_save.connect(question_post_save, sender=Choice)
