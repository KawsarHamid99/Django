from django.urls import path
from . import views

urlpatterns=[
    path("pagination/",views.pagination),
    path("",views.MainView.as_view(),name='main-view'),
    path("posts-json/<int:num_post>/",views.PostJsonListView.as_view(),name='posts-json-view'),
    
]