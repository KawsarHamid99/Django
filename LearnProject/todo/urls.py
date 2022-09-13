from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.index,name="home"),
    path("create_todo/",views.create_todo,name="create_todo"),
]