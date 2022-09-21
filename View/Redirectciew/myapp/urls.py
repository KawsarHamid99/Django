from django.views.generic import TemplateView,RedirectView

from django.urls import path
from . import views
urlpatterns=[  
    path("",TemplateView.as_view(template_name="base.html"),name="templateview"),
    path('homes/',RedirectView.as_view(url='/'),name="home"),
    path('index/',RedirectView.as_view(url='/homes/'),name="index"),
    path('fb/',views.youtubeView.as_view(),name='youtube'),
    path("home/<int:pk>/",views.GeeckRedirectView.as_view(),name="geeck"),
    path('<int:pk>/',views.TemplateView.as_view(template_name='base.html'),name='mindex'),

]