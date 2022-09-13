from django.urls import path
from . import views

urlpatterns=[ 
    path("",views.home,name="signup1"),
    path("login",views.user_login,name="login1"),
    path("profile",views.user_profile,name="profile1"),
    path("logout",views.user_logout,name="logout1"),
    path("passwordChange1",views.passwordChangeWithOld,name="passwordChange1"),
    path("passwordChangeWithoutold",views.passwordChangeWithoutold,name="passwordChangeWithoutold"),
]