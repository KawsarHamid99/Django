from django.contrib import admin
from .models import Studentlist
# Register your models here.

@admin.register(Studentlist)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","name","email",'faculty']