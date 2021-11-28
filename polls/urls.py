from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('comment/create/<int:question_id>/', views.comment_create, name='comment_create'),
    path('update/<int:question_id>/<int:comment_id>', views.comment_update, name='comment_update'),
    path('delete/<int:question_id>/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('recooment_create/<int:question_id>', views.recomment_create, name='recomment_create'),
    path('search/', views.globalsearch, name='globalsearch'),
    path('suggestion/create/<int:question_id>', views.suggestion, name='suggestion'),


]
