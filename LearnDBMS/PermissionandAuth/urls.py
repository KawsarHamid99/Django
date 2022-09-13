from django.urls import path
from . import views

urlpatterns=[
    path("permission",views.PermissionandAuthorization,name="permission")
]