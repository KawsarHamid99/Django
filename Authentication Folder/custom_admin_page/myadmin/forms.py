from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    password2=forms.CharField(label="Confirm Password" ,widget=forms.PasswordInput())
    password1=forms.CharField(label="Password" ,widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name',"last_name","email"]


class EditUserForm(UserChangeForm):
    password=None 
    class Meta:
        model=User
        fields=["username",'first_name',"last_name","email","last_login","date_joined","is_active"]

class EditAdminForm(UserChangeForm):
    class Meta:
        model=User
        fields="__all__"