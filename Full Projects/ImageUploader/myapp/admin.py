from atexit import register
from django.contrib import admin
from .models import image
# Register your models here.
@admin.register(image)
class Imageadmin(admin.ModelAdmin):
    list_display=["id","photo",'date']
