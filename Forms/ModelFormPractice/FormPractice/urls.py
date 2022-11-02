from django.urls import path
from . import views

urlpatterns=[ 
    path("home/",views.home,name="home"),
    path("",views.registration2,name="registration2"),
]