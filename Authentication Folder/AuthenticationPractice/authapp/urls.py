from django.urls import path

from . import views

urlpatterns=[ 
    path("",views.func,name="home"),
    path("login/",views.user_login,name="home")
]