from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password (Again)',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=["username",'first_name',"last_name",'email',"date_joined","last_login"]


class EditAdminProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'