from django.contrib import admin
from django.urls import path
from pro1 import views

urlpatterns = [
    path('greet/',views.greetings),

]
