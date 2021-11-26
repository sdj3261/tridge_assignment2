from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('comment/create/<int:question_id>/', views.comment_create, name='comment_create'),
    path('reply/<int:comment_pk>/', views.reply_create, name='reply_create'),
    path('search/', views.globalsearch),
    path('suggestion/create/<int:question_id>', views.suggestion, name='suggestion'),
]
