from django.contrib import admin

from .models import Teacher,student


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display=["name",'empnum',"city","salary","join_date"]



@admin.register(student)
class AdminStudent(admin.ModelAdmin):
    list_display=["name","roll","city","marks","pass_date","admitdate"]




