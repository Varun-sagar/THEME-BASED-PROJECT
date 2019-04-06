
from django.db import models
from django.contrib.auth.models import User


class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40)
    pass_word = models.CharField(max_length=20)
    status = models.BooleanField()
    img=models.ImageField(null=True,upload_to='images/')

    def __str__(self):

        return self.user_name


class Corporate(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    pass_word=models.CharField(max_length=25)
    cname=models.CharField(max_length=40)

    def __str__(self):
        return self.cname

import datetime
from django.utils.translation import ugettext_lazy as _

class event_creation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name =models.CharField(max_length=100)
    event_location =models.CharField(max_length=40)
    start_date = models.DateField(_("Start_Date"), default=datetime.date.today)
    end_date =  models.DateField(_("end_Date"), default=datetime.date.today)
    numv =models.IntegerField(default=0)
    def __str__(self):
        return self.event_name

    def user_can_vote(self, user):
        user_votes=user.vote_set.all()
        qs=user_votes.filter(event=self)
        if qs.exists():
            return False
        return True
    @property
    def num_votes(self):
        return self.vote_set.count()


class vote(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(event_creation,on_delete=models.CASCADE)



class languages(models.Model):
    lang=models.CharField(max_length=10)
    def __str__(self):
        return self.lang


class person(models.Model):
    name=models.CharField(max_length=30)
    languages =models.ManyToManyField(languages)
    def __str__(self):
        return self.name



class event_contrib(models.Model):
    user=models.ForeignKey(User,on_delete='CASCADE')
    event_id=models.ForeignKey(event_creation,on_delete='CASCADE')
    company_name =models.CharField(max_length=30)
    budget=models.IntegerField()

    def __str(self):
        return self.event_id

    class Meta:
        unique_together = ("user","event_id","company_name")