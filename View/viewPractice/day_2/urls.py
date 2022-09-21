from distutils.log import info
from django.urls import path
from . import views
urlpatterns=[ 
    path("registration",views.registration.as_view(),name='registration'),
    path("inform/",views.inform.as_view(age=22),name='inform'),
    path('home/',views.HomeView.as_view(extra_context={'course':'Python'}),name="home"),
    path('',views.contactView.as_view(extra_context={'course':120}),name='contact'),
    path('xview/',views.xview.as_view(extra_context={'course':230}),name='xview'),

]