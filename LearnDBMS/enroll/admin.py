from django.contrib import admin

# Register your models here.
from enroll.models import Student
@admin.register(Student)
class adminStudent(admin.ModelAdmin):
    list_display=("id","stuid","stumail","stupass")
#admin.site.register(Student,adminStudent)
