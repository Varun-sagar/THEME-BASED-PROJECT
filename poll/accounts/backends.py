
from .models import Individual

class IndividualBackend(object):

    def authenticate(self,user_name=None,pass_word=None,**kwargs):
        try:
            user=Individual.objects.get(user_name=user_name)

        except Individual.MultipleObjectsReturned:
            user=Individual.objects.filter(user_name=user_name).order_by('id')[0]
            return user
        except Individual.DoesNotExist:
            return None


        return user

    def get_user(self,user_id):
        try:
           return Individual.objects.get(pk=user_id)
        except Individual.DoesNotExist:
            return None
