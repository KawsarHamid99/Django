from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[  
    path("",views.home,name="home"),
    path('HomeView/',views.HomeView.as_view(),name="HomeView"),
]