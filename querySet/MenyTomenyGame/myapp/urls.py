from django.urls import path
from . import views


urlpatterns=[
    path("",views.home),
    path("<int:id>",views.home),
    path('get_related_info/<int:processor_id>/', views.get_related_info, name='get_related_info'),
    path('filterbyRam/<int:processor_id>/', views.filterbyRam, name='filterbyRam'),
]