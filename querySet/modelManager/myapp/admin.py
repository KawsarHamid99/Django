from django.contrib import admin
from .models import Student,Proxystudent
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id",'name','roll']
    
@admin.register(Proxystudent)
class StudentAdmins(admin.ModelAdmin):
    list_display=["id",'name','roll']
    