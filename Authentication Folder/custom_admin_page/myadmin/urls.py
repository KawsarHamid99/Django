from django.urls import path
from . import views

urlpatterns=[ 
    path("registration/",views.User_Registration,name="registration"),
    path("",views.User_login,name="login"),
    path("login/",views.User_login,name="login2"),
    path("profile/",views.user_profile,name="profile"),
    path("logout/",views.user_logout,name="logout"),
    path("changepassword/",views.user_passwordChange,name="changepassword"),
    path("setpassword/",views.set_userpassowrd,name="setpassword"),
    path("edit_user/<int:id>/",views.edit_user,name="edit_user"),
    path("permission/",views.permission_dashboard,name="permission"),
]