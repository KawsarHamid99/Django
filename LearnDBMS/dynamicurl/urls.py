from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[ 
    path("dynamic/<int:my_id>/",views.dynamic,name="stud"),
    path("",views.home,name="home"),

]