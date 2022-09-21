from django.urls import path
from redirectViews import views

urlpatterns=[  
    path("",views.TemplateView.as_view(template_name="bases.html"),name="template"),
    path("home/",views.RedirectView.as_view(url='/'),name='ho'),
    path("contact",views.RedirectView.as_view(url='/home/'),name='co'),

    path("home/<int:pk>/",views.RedirectView.as_view(pattern_name='user'),name="useprofile"),
    path("<int:pk>/",views.TemplateView.as_view(template_name="bases.html"),name="user"),
    
]