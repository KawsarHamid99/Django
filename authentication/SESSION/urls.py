from django.urls import path
from . import views

urlpatterns=[ 
    path("get",views.get_session,name="get"),
    path("set",views.set_session,name="set"),
    path("delete",views.delete_session,name="delete"),
    path("flush",views.FLUSH_session,name="flush"),
    path("settestcookie",views.settestcookie,name="settestcookie"),
    path("checktestcookie",views.checktestcookie,name="checktestcookie"),
    path("deltestcookie",views.deltestcookie,name="deltestcookie"),
]