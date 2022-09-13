from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms



class signUp_form(UserCreationForm):
    password2=forms.CharField(label='retype password',widget=forms.PasswordInput)
    class Meta:
        model=User

        fields=["username","email","first_name","last_name"]
        labels={"email":"Email"}

class EditUserM(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","last_login","is_active","date_joined"]
        labels={"email":"Email"}