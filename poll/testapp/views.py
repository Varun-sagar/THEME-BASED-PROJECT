from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Question,Cho
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'testapp/index.html', context)




def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'testapp/detail.html', {'question': question})





@login_required
def vote(request,question_id):
    print(request.POST)

    print(dir(request),request.user)
    question = get_object_or_404(Question, pk=question_id)
    print(question.pub_date)
    if request.POST.get('choice'):
        selected_choice = question.cho_set.get(pk=request.POST.get('choice'))
        print(request.user.is_authenticated)
        #poll = question
        selected_choice.votes += 1
        selected_choice.save()
    else:
        messages.error(request, 'NO choice!')
        return HttpResponseRedirect(reverse('testapp:detail', args=(question.id,)))

    return render(request, 'testapp/results.html', {'poll': question})




from django.http import HttpResponse
from django.views import View



class MyView(View):
    def get(self, request):
        # <view logic>
        print(dir(self))
        print(MyView.as_view.__doc__)
        return HttpResponse('result')