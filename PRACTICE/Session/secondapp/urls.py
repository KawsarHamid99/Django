from django.urls import path
from . import views

urlpatterns=[
    path("",views.setsession,name="setsession"),
    path("getsession/",views.getsession,name="getsession"),
    path("delete/",views.delsession,name="delsession"),
    path("flush/",views.flushsession,name="flush"),
]