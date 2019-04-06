from django.contrib import admin
from .models import employee
# Register your models here.


class emp(admin.ModelAdmin):
    list_display = ['eno','erole','ename','esal']

admin.site.register(employee,emp)




