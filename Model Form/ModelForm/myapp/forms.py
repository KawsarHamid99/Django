from distutils.log import error
from tkinter import Widget
from unicodedata import name
from django import forms 
from .models import StudentModel

class StudentForm(forms.ModelForm):
    # This "name" field will override the model name field.
    name=forms.CharField(max_length=70,widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}))
    #name=forms.CharField(max_length=70,required=False)

    class Meta:
        
        model=StudentModel
        fields=['name','email','password']
        labels={'name': "NAME",'email':"EMAIL",'password':'PASSWORD'}
        help_text={'name':"Enter Your Name"}
        error_messages={'name':{'required':'Name is required'},'email':{"required":"email is required"}}
        widgets={
            'password': forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'Enter Your Name'}) 
            }
