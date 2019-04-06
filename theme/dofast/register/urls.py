"""dofast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *
app_name ='accounts'

urlpatterns = [
    path('',index.as_view(),name='Index'),
    path('edit_profile/',edit_profile,name="edit_profile"),
    path('change_password/', change_password , name="change_password"),

    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),

    path('register/',Register.as_view(),name='Register'),
    path('Thanks/',Thanks.as_view(),name='Thanks'),
]
