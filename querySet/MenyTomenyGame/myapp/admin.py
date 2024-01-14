from django.contrib import admin

# Register your models here.
from .models import RAM,SSD,Processor,Product


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display=["id",'name','size']


@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):
    list_display=["id",'name','ram_list','size']


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display=["id",'name','size','ram_list','ssd_list']

@admin.register(Product)
class ProcessorAdmin(admin.ModelAdmin):
    list_display=["id",'name','processor_list']
