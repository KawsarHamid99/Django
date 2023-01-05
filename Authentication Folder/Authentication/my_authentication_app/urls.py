from django.urls import path

from . import views

urlpatterns=[ 
    path("home",views.home,name="home"),
    path("SignupForm",views.SignupForms,name="SignupForm"),
    path("",views.user_login,name="login"),
    path("login/",views.user_login,name="l"),
    path("profile/",views.details,name="profile"),
    path("logout/",views.logout_user,name="logout"),
    #with old passowrd
    path("changepass/",views.user_changepass, name="changepass"),
    #without old passowrd
    path("chng_pass/",views.user_changepass_without_old, name="passwordchange"),
    #Permission_Based_Profile
    path("Permission_Based_Profile/",views.Permission_Based_Profile, name="Permission_Based_Profile"),

    path("userdetails/<int:id>/",views.user_details, name="userdetails"),
    path("dashboard/",views.dashboard, name="dashboard"),
]