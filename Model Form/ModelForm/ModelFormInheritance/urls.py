import imp
from django.urls import path

from . import views

urlpatterns=[ 
    path("",views.StudentView,name="studentView"),
    path("teacherView",views.TeacherView,name="TeacherView")
]