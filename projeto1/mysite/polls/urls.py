from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path


from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('<int:pk>/', views.detailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.resultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('specifics/<int:question_id>/', views.detail, name='detail'),
]