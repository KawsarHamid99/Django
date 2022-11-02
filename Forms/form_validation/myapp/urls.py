from django.urls import path
from . import views 

urlpatterns=[
    path("",views.showFormData,name="home"),
    path("success/",views.success,name="suc"),
]