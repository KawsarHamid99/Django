from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[  
    #path("",views.home,name="home"),
    path("",views.TemplateView.as_view(template_name='base.html')),
    path("count/",views.HomeView.as_view(),name="count"),
    path('context',views.contextView.as_view(extra_context={'course':'Python'}),name="context"),
    path('profile/<int:class>',views.contextView.as_view(extra_context={'course':'Python'}),name="context"),
]