from django.contrib import admin
from .models import Individual,Corporate,User,event_creation,vote,languages,person,event_contrib
# Register your models here.



class _event_creation_admin(admin.ModelAdmin):
    list_display = ['id','event_name','event_location']


admin.site.register(vote)
admin.site.register(Individual)
admin.site.register(Corporate)
admin.site.register(event_creation,_event_creation_admin)

admin.site.register(languages)
admin.site.register(person)
admin.site.register(event_contrib)



