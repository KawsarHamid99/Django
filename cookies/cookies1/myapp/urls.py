from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("getcookies",views.getcookies,name="getcookies"),
    path("delcookies",views.delcookies,name="delcookies"),

]