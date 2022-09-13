from django.urls import path
from . import views
urlpatterns=[
    path("",views.Home,name="home"),
    path("delete/<int:id>/",views.delete_data,name="delete"),
    path("update/<int:id>/",views.update_data,name="update"),
]