from django.urls import path
from . import views

urlpatterns = [
    path('admin/get_user_profiles/', views.get_user_profiles, name='get_user_profiles'),
    # other URL patterns
]
