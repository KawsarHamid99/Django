from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[ 
    path("",views.home,name="home"),
    path("forms",views.stuForm,name="forms"),
    path("forms2",views.form2,name="forms2"),
]