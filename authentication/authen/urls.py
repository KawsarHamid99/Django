from django.urls import path
from . import views


urlpatterns=[ 
    path("",views.home,name="signup"),
    path("login",views.user_Login,name="login"),
    path("profile",views.user_profile,name="profile"),
    path("logout",views.user_logout,name="logout"),
    path("changePassword",views.user_changePassword,name="changePassword"),
    path("userdetails/<int:id>",views.user_details,name="userdetails"),
    path("user_changePassword_withoutold",views.user_changePassword_withoutold,name="user_changePassword_withoutold"),
]