from django.contrib import admin
from .models import * 
# Register your models here.

class PersonModel(admin.ModelAdmin):
    list_display=["name",'mobile','written_by']
admin.site.register(Person,PersonModel)
admin.site.register([Interest,City,Personaddress])