from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("delete/<int:id>",views.delete_data,name="detetedata"),
    path("update/<int:id>",views.update_data,name="updatedata"),
]