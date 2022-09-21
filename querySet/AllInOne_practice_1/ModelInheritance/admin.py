from django.contrib import admin

# Register your models here.
from .models import parent,child,contractor,Student,Teacher,father,son

@admin.register(parent)
class parentAdmin(admin.ModelAdmin):
    list_display=['color','height']



@admin.register(child)
class childAdmin(admin.ModelAdmin):
    list_display=['color','height','name','age']

@admin.register(father)
class fatherAdmin(admin.ModelAdmin):
    list_display=['name','age','clr']

@admin.register(son)
class sonAdmin(admin.ModelAdmin):
    list_display=['name','age','clr']