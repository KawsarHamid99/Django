from unicodedata import name
from django import forms 

class studentRegistration(forms.Form):
    #error_css_class='error'
    name=forms.CharField(error_messages={'required':'Enter Your Name'})
    email=forms.EmailField(min_length=2 ,error_messages={'required':'Enter your Email'})
    password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Type Your Password'})    