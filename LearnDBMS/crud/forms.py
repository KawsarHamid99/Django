from dataclasses import fields
from tkinter import Widget
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']

        #create all attribute
        #fields="__all__"

        #Except name attribute
        #exclude=["name"]


        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
        }