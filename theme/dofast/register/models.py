from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_individual = models.BooleanField(default=False)
    is_corporate = models.BooleanField(default=False)


class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40)
    pass_word = models.CharField(max_length=20)
    status = models.BooleanField()
    img=models.ImageField(null=True)
    def __str__(self):

        return self.user_name


class Corporate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    pass_word=models.CharField(max_length=25)
    cname=models.CharField(max_length=40)
    service=models.CharField(max_length=40)


    def __str__(self):
        return self.user_name

