
from django.db import models
from django.contrib.auth.models import User


class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40)
    pass_word = models.CharField(max_length=20)
    status = models.BooleanField()

    def __str__(self):

        return self.user_name



class Corporate(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    pass_word=models.CharField(max_length=25)
    cname=models.CharField(max_length=40)

    def __str__(self):
        return self.cname

