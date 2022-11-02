from django.urls import path
from . import views 

urlpatterns=[
    path("home/",views.showFormData,name="home"),
    path("morefield",views.MoreOnFormView,name="morefield"),
    path("",views.formRegistration,name=""),
    path("password",views.passwordValidation,name="password"),
]