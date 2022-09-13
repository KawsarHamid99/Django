from django.urls import path
from . import views
urlpatterns=[
    path("",views.Signup,name="signup"),
    path("Signup2",views.Signup2,name="signup"),
    path("login",views.Login,name="login"),
    path("profile",views.profile,name="profile"),
    path("logout",views.Logout,name="logout"),
    path("changepass",views.changepass,name="changepass"),
    path("user_details/<int:id>",views.user_details,name="user_details"),
    path("changepassWithoutOld",views.changepassWithoutOld,name="changepassWithoutOld"),
    path("dashboard",views.user_dashboard,name="dashboard"),
]