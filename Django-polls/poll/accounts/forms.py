

from django import forms

class User_Form(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password= forms.CharField(label='Your password', max_length=100)




from .models import Individual
from django.forms import ModelForm
from django.core.exceptions import ValidationError



class IndividualForm(ModelForm):
    class Meta:
        model=Individual
        fields='__all__'

    def clean_user_name(self):
        p1 = self.cleaned_data['user_name']
        if len(p1)==3:
            raise ValidationError("less length")
        return p1
# Create your models here.



from .models import Corporate

from django.forms import ModelForm

class CorporateForm(ModelForm):
    class Meta:
        model = Corporate
        fields = '__all__'


from .models import event_creation,person,languages

class eventform(ModelForm):
    class Meta:
        model = event_creation
        exclude =('user',)



class editform(ModelForm):
    class Meta:
        model =event_creation
        fields ='__all__'



class per(ModelForm):
    class Meta:
        model =person
        fields ='__all__'
