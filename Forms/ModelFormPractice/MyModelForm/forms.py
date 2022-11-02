from multiprocessing.sharedctypes import Value
from socket import fromshare
from tkinter import Widget
from django import forms

from django.core import validators

from .models import Student

class StudentForm(forms.ModelForm):
    name=forms.CharField(error_messages={'required':"name can not me empty"})
    class Meta:
        model=Student
        fields=["name",'email','dept','password']
        labels={'name':"NAME",'email':"EMAIL",'dept':"DEPERTMENT",'password':"PASSWORD"}
        help_text={'name':'Enter Your Name'}
        error_messages={'name':{'required':"Enter Your Name"},'email':{'required':"Enter Your Email"}}
        inital={'name':"kabila"}
        widgets={
            
            'name':forms.TextInput(attrs={'class':'form-control',"placeholder":'kawsar'}),
            'email':forms.EmailInput(attrs={'class':'form-control',"placeholder":'example@gmail.com'}),
            'password':forms.PasswordInput,
        }
    
        