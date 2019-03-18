

from django import forms

class User_Form(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password= forms.CharField(label='Your password', max_length=100)




from .models import Individual
from django.forms import ModelForm



class IndividualForm(ModelForm):
    class Meta:
        model=Individual
        fields='__all__'
# Create your models here.



from .models import Corporate

from django.forms import ModelForm

class CorporateForm(ModelForm):
    class Meta:
        model = Corporate
        fields = '__all__'
