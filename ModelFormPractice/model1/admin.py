from django.contrib import admin
from .models import students
# Register your models here.


class adminStudents(admin.ModelAdmin):
    list_display=["stuid","stuname","stuemail"]
#admin.site.register(students,adminStudents)
admin.site.register(students)