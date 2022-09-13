from math import frexp
from django.urls import path
from . import views
urlpatterns=[ 
    path("",views.func,name="home")
]