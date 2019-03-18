from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from  django.urls import reverse
from django.contrib.auth.models import User
from .forms import IndividualForm,CorporateForm
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

    return render(requests,'accounts/in.html',{})







def logo(request):
    logout(request)
    return HttpResponseRedirect(reverse('testapp:index'))





from .models import Individual
def register(request,*args,**kwargs):
    #print(request.POST)
    context = {}
    l=len(request.POST)
    print(l)
    if request.method=='POST' and 'gender' not in request.POST:
        if l<=5:
            print(request.POST)
            u = IndividualForm(request.POST)
            print(u.is_valid())
            if u.is_valid():
                user_id=u.cleaned_data['user']
                username = u.cleaned_data['user_name']
                pass_word = u.cleaned_data['pass_word']
                status =u.cleaned_data['status']
                print(u.cleaned_data)

                new_individual =User.objects.create_user(username='pop',password='popsagar')

                new_individual =u.save()
                print("helo", new_individual,username,pass_word,status)
                #print(user)
                messages.success(request, 'Thanks for registring {}'.format(username))
                return redirect('accounts:log')
                #return HttpResponseRedirect(reverse('accounts:log'))
        else:
            print('*********COOL***********')

            print(request.POST)
            u = CorporateForm(request.POST)
            if u.is_valid():
                username = u.cleaned_data['cname']
                #phone = u.cleaned_data['']
                status = u.cleaned_data['service']
                print(u.cleaned_data)
                new_individual = u.save()
                print("helo", new_individual, username, status)
                # print(user)
                messages.success(request, 'Thanks for registring {}'.format(username))
                return redirect('accounts:log')

    else:
        print(request.POST)

        print(request.POST.get('gender'),type(request.POST.get('gender')))
        if(request.POST.get('gender')=='male'):
            context['gender'] = 1
        elif request.POST.get('gender')=='female':
            context['gender']=0

        print('hello')
        context['form']=None
        if context.get('gender')==1:
            form = IndividualForm()
            context['form'] = form
        elif context.get('gender')==0:
            form = CorporateForm()
            context['form'] = form


        print(context)

    return render(request,'accounts/register.html',context)



def reg(request):
    print("IN reg")
    if request.method=='POST':
        print(request.POST)
        #m={'gender': request.POST['gender']}
        return redirect('accounts:register')


from django.core.mail import send_mail


def senmail(request):
    send_mail(
        'This is Cool',
        'Here is the message.',
        'varuntejasagar016@gmail.com',
        ['ragonawom@virtual-email.com'],
        fail_silently=False,
    )

