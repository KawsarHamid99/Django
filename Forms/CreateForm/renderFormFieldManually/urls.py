from django.urls import path
from . import views 

urlpatterns=[
    path("",views.showFormData,name="home"),
]