from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data published')

    def __str__(self):
        return str(self.Question_text)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Cho(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        #s=""
        return self.choice_text



from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)


    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class link(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

