from django.urls import path
from . import views
urlpatterns=[ 
    path("Myview/",views.Myview.as_view(age='bakis'),name='Myview'),
    path("Myview/",views.HomeClass.as_view(),name="Myview"),
    path("contactfunc/",views.cf,name="contact"), 
    path("",views.contactForm.as_view(),name="contactform")
]