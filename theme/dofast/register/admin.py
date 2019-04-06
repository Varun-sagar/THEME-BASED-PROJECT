from django.contrib import admin

# Register your models here.

from .models import  User,Individual,Corporate
admin.site.register(User)
admin.site.register(Corporate)
admin.site.register(Individual)

