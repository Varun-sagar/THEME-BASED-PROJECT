from django.db import models

# Create your models here.

class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=70)
    esal=models.IntegerField()
    erole=models.CharField(max_length=25)
    feature=models.BooleanField()
    def __str__(self):
        return self.erole