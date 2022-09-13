from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns=[ 
    path("",views.home,name="home"),
    path("home",views.home2,name="home2"),
    path("contact",cache_page(20)(views.contact),name="contact"),
    path("base",views.base,name="base"),
    path("dlt",views.delete,name="dlt"),
    path("clr",views.clr_cache,name="clr"),
]