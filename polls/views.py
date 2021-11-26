import requests
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.db.models import F
from utils.url import restify
from .forms import CommentForm
from .models import Choice, Question, Comment
from .serializers import QuestionSerializer

CHOICE_LIMIT = 5

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        response = requests.get(restify("/questions/"))
        questions = response.json()
        return questions[:5]


class DetailView(generic.DetailView):
    model = Question
    queryset = model.objects.filter(is_public=True)
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = self.object.comment_set.filter(parent__isnull=True)
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # selected_choice.votes += 1
        # Use mutex_lock, Solve Race Condition
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def index(request):
    return render(request, "polls/index.html")


@login_required
def comment_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.comment_set.create(content=request.POST.get('content'))
    return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))

@login_required
def reply_create(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    question = comment.question
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.parent = comment
        reply.question = question
        reply.save()
        return redirect('polls:detail', pk=question.id)
    context = {
        'form': form,
        'question': question,
        'comment': comment,
    }
    return render(request, 'polls:detail', context)

@login_required
def globalsearch(request):
    qs = Question.objects.all()
    qs2 = Choice.objects.all()
    result = qs.union(qs2)
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'polls/search/globalsearch.html', {
        'globalsearch': qs,
    })

@login_required
def suggestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_count = Choice.objects.filter(question=question).count()
    if request.method == 'POST' and choice_count < CHOICE_LIMIT:
        Choice.objects.create(
            question=question,
            choice_text=request.POST['text'],
        )

    return redirect('polls:detail', pk=question.id)


# API
# ===


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
