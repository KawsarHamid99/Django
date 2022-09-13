from django.urls import path
from . import views
urlpatterns=[ 
    path("",views.home,name="home"),
    path("excp",views.excp,name="excp"),
    path("context",views.user_info,name="context"),
]