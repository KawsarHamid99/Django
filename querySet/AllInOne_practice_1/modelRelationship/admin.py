from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','first_name','last_name','email']

@admin.register(page)
class pageAdmin(admin.ModelAdmin):
    list_display=['user_id','page_name','page_cat',"page_publish_date"] 


@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=['user_id','post_title','post_cat','post_publish_date']


@admin.register(song)
class SongAdmin(admin.ModelAdmin):
    list_display=['song_name','song_duration','written_by']
