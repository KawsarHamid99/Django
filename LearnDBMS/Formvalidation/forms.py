import email
from django import forms
from .models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']

    #name=forms.CharField()
    #email=forms.EmailField()
    #password=forms.CharField(widget=forms.PasswordInput)