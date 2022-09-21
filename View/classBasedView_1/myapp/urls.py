from django.urls import path
from . import views

urlpatterns=[  
    path("func/",views.home,name="home"),
    path("cl/",views.myview.as_view(),name="classbased"),
    path('cl2/',views.myview.as_view(name="kabila"),name="cl2"),
    path('subcl/',views.childclass.as_view(),name="subcl"),
    path('',views.HomeClassView.as_view(),name="homeclass"),


    path("contact/",views.contactfun,name="contact"),
    path('contactClass/',views.ContactClassView.as_view(),name="contactClass"),
]