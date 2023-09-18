from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("charge/<int:pk>",views.charge,name="charge")
]