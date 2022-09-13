from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms 

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label="retype password ",widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]
        labels={"email":"Email"}


class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","date_joined","last_login"]
        labels={"email":"Email"}


class EditAdminProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields="__all__"
        labels={"email":"Email"}