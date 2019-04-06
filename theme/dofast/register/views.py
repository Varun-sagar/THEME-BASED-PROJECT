from django.shortcuts import render
from django.contrib import messages
from .forms import IndividualForm,CorporateForm,editprofileform
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from .models import Individual,Corporate
from .models import User
from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.models import User
from django.http import  HttpResponse

from django.contrib.auth.hashers import make_password

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


def edit_profile(request):
    if request.method =="POST":
        form =editprofileform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return render(request,'register/index.html',{})
    else:
        form =  editprofileform(instance=request.user)
        args ={'form':form}
        return render(request,'register/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method =="POST":
        print(request.POST)
        form = PasswordChangeForm(user=request.user,data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("cool")
            print(request.user)
            update_session_auth_hash(request,form.user)
            return render(request,'register/index.html',{})
            #render(request,'register/edit_profile.html',{})
    else:
        form = PasswordChangeForm(user=request.user)
        args ={'form':form}
        return render(request,'register/change_password.html',args)



class Thanks(TemplateView):
    template_name = "register/thanks.html"


class index(TemplateView):
    template_name = 'register/index.html'





class Register(View):


    '''

          context = {}
    l=len(request.POST)
    print(l)
    if request.method=='POST' and 'gender' not in request.POST:
        if l<=5:
            print(request.POST)
            u = IndividualForm(request.POST)
            print(u.is_valid())
            print(u.errors)
            if u.is_valid():
                user_id=u.cleaned_data['user']
                username = u.cleaned_data['user_name']
                pass_word = u.cleaned_data['pass_word']
                status =u.cleaned_data['status']
                print(u.cleaned_data)
                user = User.objects.create_user(username=username, password=password)

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

    '''

    def post(self, request, *args, **kwargs):
        context={}
        if request.method=='POST' and 'gender' not in request.POST:
            l=len(request.POST)
            if l == 4:
                u = IndividualForm(request.POST,request.FILES)
                print(u.is_valid())
                if u.is_valid():
                    username = u.cleaned_data['user_name']
                    pass_word = u.cleaned_data['pass_word']



                    enc_password=make_password(pass_word)
                    user = User(username=username, password=enc_password)
                    user.is_individual = True
                    user.is_corporate = False
                    user.save()
                    print(user)
                    use = User.objects.get(username=username)
                    c=u.save(commit=False)
                    c.user = use
                    c.save()
                    messages.success(request, 'Thanks for registring {}'.format(username))
                    return redirect('accounts:Login')
            else:
                u = CorporateForm(request.POST)
                if u.is_valid():
                    username = u.cleaned_data['user_name']
                    pass_word = u.cleaned_data['pass_word']
                    enc_password = make_password(pass_word)
                    user = User(username=username, password=enc_password)
                    user.is_corporate = True
                    user.save()
                    c = u.save(commit=False)
                    use = User.objects.get(username=username)
                    c.user = use
                    c.save()
                    messages.success(request, 'Thanks for registring {}'.format(username))
                    messages.success(request, 'Thanks for registring {}'.format(username))
                    return redirect('accounts:Login')

        else:
            if (request.POST.get('gender') == 'male'):
                context['gender'] = 1
            elif request.POST.get('gender') == 'female':
                context['gender'] = 0

            context['form'] = None
            if context.get('gender') == 1:
                form = IndividualForm()
                context['form'] = form
            elif context.get('gender') == 0:
                form = CorporateForm()
                context['form'] = form
        return render(request, 'register/register_form.html', context)




    def get(self,request,*args,**kwargs):
        context={}
        return render(request, 'register/register_form.html', context)




class Login(View):

    def post(self,requests,*args,**kwargs):
        print(requests.user)
        print(requests.method)
        print(requests.POST)
        l=len(requests.POST)
        if requests.method == 'POST' and 'gender' not in requests.POST:
            if l==3:
                username = requests.POST.get('username')
                password = requests.POST.get('password')
                print(username)
                print(password)
                user = authenticate(requests, username=username, password=password)
                print(user)

                if user is not None:
                    u= User.objects.get(username=username)
                    if u.is_individual == True and u.is_corporate == False:
                        login(requests, user)
                    return redirect('accounts:Index')
                else:
                    messages.error(requests, 'Bad request')
                    return redirect('accounts:Index')

            else:
                username = requests.POST.get('username')
                password = requests.POST.get('password')
                cin=requests.POST.get('cin')
                print(username)
                print(password)
                user = authenticate(requests, username=username, password=password)
                print(user)
                if user is not None:
                    u = Corporate.objects.get(user_name=username)
                    if u.cname == cin:
                        login(requests, user)
                    return redirect('accounts:Index')
                else:
                    messages.error(requests, 'Bad request')
                    return redirect('accounts:Index')







        else:
            context={}
            if (requests.POST.get('gender') == 'male'):
                context['gender'] = 1
            elif requests.POST.get('gender') == 'female':
                context['gender'] = 0

            context['form'] = None
            if context.get('gender') == 1:
                form = IndividualForm()
                context['form'] = form
            elif context.get('gender') == 0:
                form = CorporateForm()
                context['form'] = form
        return render(requests, 'register/login_form.html', context)



    def get(self,requests,*args,**kwargs):
        return render(requests, 'register/login_form.html', {})



class Logout(View):
    def get(self,requests,*args,**kwargs):
        logout(requests)
        return redirect('accounts:Index')

