from django.contrib import admin
from .models import StudentModels
# Register your models here.
@admin.register(StudentModels)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id',"name",'email','password']