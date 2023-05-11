from django.urls import path

from . import views

urlpatterns=[ 
    path("",views.func,name="home"),
    path("login/",views.user_login,name="login"),
    path("signup/",views.signup_form,name="signup"),  
    #path("profile/",views.user_details,name="profile"),  
    path("profile/",views.permissionBasesProfile,name="profile"),  
    path("user_info/<int:id>/",views.user_info,name="user_info"),  
    path("logout/",views.user_logout,name="logout"),  
    path("ChangePassword/",views.ChangePassword,name="ChangePassword"),  
    path("set_password/",views.set_password,name="set_password"),  
    path("dashboard/",views.dashboard,name="dashboard"),  
]