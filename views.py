from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from  django.urls import reverse
from django.contrib.auth.models import User
from .forms import User_Form
from django.shortcuts import redirect
def logg(requests):
    print(requests.method)
    print(requests.POST)

    if requests.method=='POST':
        username=requests.POST.get('username')
        password=requests.POST.get('password')
        user= authenticate(requests,username=username,password=password)
        print(user)
        if user is not None:
            login(requests, user)
            return HttpResponseRedirect(reverse('testapp:index'))
        else:
            messages.error(requests, 'Bad request')

    return render(requests, 'accounts/in.html',{})

def logo(request):
    logout(request)
    return HttpResponseRedirect(reverse('testapp:index'))

def register(request):
    print("helo")

    if request.method=='POST':
        u=User_Form(request.POST)
        if u.is_valid():
            username = u.cleaned_data['username']
            password = u.cleaned_data['password']
            print(u.cleaned_data)
            user = User.objects.create_user(username=username, password=password)
            print("helo")
            print(user)
            messages.success(request,'Thanks for registring {}'.format(user.username))
            return redirect('accounts:log')
            #return HttpResponseRedirect(reverse('accounts:log'))
    else:
        print('hello')
        form=User_Form()
    return render(request,'accounts/register.html',{'form':form})