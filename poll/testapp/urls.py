from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name='testapp'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('class/', views.MyView.as_view(), name='cool'),
    path('about/', login_required(TemplateView.as_view(template_name="testapp/detail.html")))
]
