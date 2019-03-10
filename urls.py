from django.urls import path

from . import views

app_name='accounts'

urlpatterns = [
    # ex: /polls
    path('login/', views.logg, name='log'),
    path('logout', views.logo, name='logout'),
    path('register',views.register,name='register'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
