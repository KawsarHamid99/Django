from django.contrib import admin
from .models import Mother,daughter
# Register your models here.

@admin.register(Mother)
class motherAdmin(admin.ModelAdmin):
    list_display=["name",'age']


@admin.register(daughter)
class daughterAdmin(admin.ModelAdmin):
    list_display=['name','age']
