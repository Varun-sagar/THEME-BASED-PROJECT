from django.urls import path

from . import views

app_name ='accounts'

urlpatterns = [
 #accounts
    path('person/',views.person,name='person'),
    path('',views.index, name="Index"),
    path('details/<int:id>/',views.detail,name='details'),
    path('edit/<int:id>/', views.edit_event, name="edit_event"),
    path('eventform/', views.event, name="eventform"),
    path('login/', views.logg, name='log'),
    path('logout/', views.logo, name='logout'),
    path('register/',views.register,name='register'),
]
