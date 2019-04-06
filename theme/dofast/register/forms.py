







from .models import Individual,User
from django.forms import ModelForm



class IndividualForm(ModelForm):
    class Meta:
        model=Individual
        exclude=('user',)
# Create your models here.



from .models import Corporate

from django.forms import ModelForm

class CorporateForm(ModelForm):
    class Meta:
        model = Corporate
        exclude=('user',)


from django.contrib.auth.forms import UserChangeForm


class editprofileform(UserChangeForm):
    class Meta:
        model = User
        fields =('username',
                  'email',
                 'password',

                 )


