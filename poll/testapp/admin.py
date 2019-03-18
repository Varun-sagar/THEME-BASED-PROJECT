from django.contrib import admin
from .models import Question,Cho
# Register your models here.

from .models import Cho,Question

class Cho_admin(admin.ModelAdmin):
    list_display = ['id','question','choice_text','votes']


admin.site.register(Question)
admin.site.register(Cho,Cho_admin)
#admin.site.register(In)