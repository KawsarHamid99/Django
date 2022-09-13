from django.urls import path
from . import views
urlpatterns=[
    path("set",views.home,name="set"),
    path("get",views.get_cookies,name="get"),
    path("del",views.del_cookies,name="del"),
]