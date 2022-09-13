from django.contrib import admin
from .models import St,Teacher,Contractor,parents,Child,son,father
from myapp import models
# Register your models here.
@admin.register(St)
class StudentAdmin(admin.ModelAdmin):
    list_display=["name",'age']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=["name","age"]

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['name','age']


class parentsAdmin(admin.ModelAdmin):
    list_display=["id",'clr','height']
admin.site.register(parents,parentsAdmin)

class childAdmin(admin.ModelAdmin):
    list_display=["name","age","clr",'id','height']
admin.site.register(Child,childAdmin)

class fatherAdmin(admin.ModelAdmin):
    list_display=['id','name',"age",'clr']
admin.site.register(father,fatherAdmin)

class sonAdmin(admin.ModelAdmin):
    list_display=['id','name',"age",'clr']
admin.site.register(son,sonAdmin)