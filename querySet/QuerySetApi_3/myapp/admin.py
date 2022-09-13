from django.contrib import admin
from .models import student,Teacher
# Register your models here.
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date','admitdate']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display= ["name","empnum","city","salary","join_date"]
