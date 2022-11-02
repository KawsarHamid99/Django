from django.urls import path

from . import views

urlpatterns=[ 
    path("home",views.home,name="home"),
    path("SignupForm",views.SignupForms,name="SignupForm"),
    path("",views.user_login,name="login"),
    path("login/",views.user_login,name="l"),
    path("profile/",views.details,name="profile"),
    path("logout/",views.logout_user,name="logout"),
]