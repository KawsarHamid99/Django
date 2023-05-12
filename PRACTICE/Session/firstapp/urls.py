from django.urls import path
from . import views


urlpatterns=[
    path("",views.setsession,name="sessionset"),
    path("get",views.getsession,name="sessionget"),
    path("del",views.delsession,name="sessiondel"),
    path("flush",views.flushsession,name="flush"),

    path("st",views.set_test_session,name="st"),
    path("ct",views.check_test_session,name="ct"),
    path("dt",views.del_test_session,name="dt"),
]