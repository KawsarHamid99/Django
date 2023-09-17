from django.contrib import admin
from .models import Home
# Register your models here.
@admin.register(Home)
class AdminHome(admin.ModelAdmin):
    list_display=["id","name","national_id","city"]