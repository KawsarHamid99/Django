from importlib.resources import path
from django.urls import path

from . import views

urlpatterns=[ 
    path("details/<int:pk>/",views.StudentDetail.as_view(),name="details")

]