from django.urls import path
from . import views

urlpatterns=[ 
    path("FormCAV",views.FormCleanAndValidating,name="FormCAV"),
]