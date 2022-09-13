from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display=["id","title","desc"]

admin.site.register(Blog,BlogModelAdmin)