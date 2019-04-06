from django.shortcuts import render
from django.http import HttpResponse
from pro1.models import employee
# Create your views here.
import datetime
def greetings(request):
    s=datetime.datetime.now()
    h=int(s.strftime("%H"))
    d={'date':s,'hour':h}
    e= employee.objects.all()
    d['employee']=e
    return render(request,'pro1/first.html',context=d)

