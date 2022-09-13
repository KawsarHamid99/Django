from django.urls import path

from QuerySetApi_3 import views
from . import views

urlpatterns=[ 
    path("",views.home,name="home")
]