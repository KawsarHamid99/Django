from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("signin/",views.user_signin,name="signin"),
    path("login/",views.user_login,name="login"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("logout/",views.user_logout,name="logout"),
    path("addpost/",views.add_post,name="addpost"),
    path("delete/<int:id>/",views.delete_post,name="delete"),
    path("updatepost/<int:id>/",views.update_post,name="updatepost"),
   
]