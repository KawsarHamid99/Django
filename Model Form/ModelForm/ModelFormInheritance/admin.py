from django.contrib import admin
from .models import Registration
# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display=["id",'student_name','teacher_name','email','age','depertment']