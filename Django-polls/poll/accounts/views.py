from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from  django.urls import reverse
from django.contrib.auth.models import User
from .forms import IndividualForm,CorporateForm,eventform,editform,per
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import event_creation,vote
from django.shortcuts import get_object_or_404
from .mail_check import make_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def person(request):
    form=per()
    return render(request,'accounts/edit_event_form.html',{'form':form})





@login_required
def detail(request,id):
    obj= get_object_or_404(event_creation,id=id)
    return render(request,'accounts/detail.html',{'obj':obj})


def logg(requests):
    print(requests.method)
    print(requests.POST)

    if requests.method =='POST':
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



@login_required
def logo(request):
    logout(request)
    return HttpResponseRedirect(reverse('testapp:index'))

@login_required
def edit_event(request,id):
    print(id)
    obj= get_object_or_404(event_creation,id=id)
    print(obj)
    if request.user!= obj.user:
        return redirect('/')

    if request.method == 'POST':
        form = editform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated!!', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('accounts:Index')

    else:
        form =editform(instance=obj)
    return render(request,'accounts/edit_event_form.html',{'form':form})


def index(requests):

    event_o = event_creation.objects.filter(user__username=requests.user)
    eventobj = event_creation.objects.exclude(user__username__contains=requests.user)
    paginator =Paginator(event_o,5)
    page = requests.GET.get('page')
    event_o =paginator.get_page(page)


    if requests.method == 'POST':
        print(requests.path)
        id = requests.POST['id']
        o = event_creation.objects.get(id=id)
        if not o.user_can_vote(requests.user):
            messages.error(requests, 'Already voted!')
            return render(requests, 'accounts/index.html', {'myself': event_o, 'others': eventobj})
        new_vote =vote(user=requests.user,event=o)
        new_vote.save()
        o.numv = o.numv + 1
        o.save()
    return render(requests,'accounts/index.html',{'myself':event_o ,'others':eventobj})


@login_required
def event(request):
    form =eventform()
    if request.method == 'POST' and request.user.is_authenticated:
        print(request.POST)

        u=eventform(request.POST)
        #make_mail(request.POST['event_name'])
        if u.is_valid():
            o=request.user
            c=u.save(commit=False)
            c.user=o
            c.save()
        messages.success(request, 'Details updated!!',extra_tags='alert alert-success alert-dismissible fade show')
        return redirect('accounts:Index')
    return render(request,'accounts/event_form.html',{'form':form})




from .models import Individual
def register(request,*args,**kwargs):
    #print(request.POST)
    context = {}
    l=len(request.POST)
    print(l)
    u=0
    if request.method=='POST' and 'gender' not in request.POST:
        if l<=6:
            print(request.POST)
            print(request.FILES)
            u = IndividualForm(request.POST,request.FILES)
            print(u.is_valid())
            print(u.errors)
            context['errors'] = u.errors
            if u.is_valid():
                user_id=u.cleaned_data['user']
                username = u.cleaned_data['user_name']
                pass_word = u.cleaned_data['pass_word']
                status =u.cleaned_data['status']
                print(u.cleaned_data)

                new_individual =User.objects.create_user(username='pop1',password='popsagar1')

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
        context['gender']=1
        print(request.POST.get('gender'),type(request.POST.get('gender')))
        if(request.POST.get('gender')=='male'):
            context['gender'] = 1
        elif request.POST.get('gender')=='female':
            context['gender']=0

        print('hello',context['gender'])

        if context.get('gender')==1:
            form = IndividualForm()
            context['form'] = form
        elif context.get('gender')==0:
            form = CorporateForm()
            context['form'] = form
        print(context)


    if 'errors' in context:
        context['form']=IndividualForm
        context['gender'] =1
        print(context)
    return render(request,'accounts/register.html',context)

'''

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

'''