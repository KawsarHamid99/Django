import email
from django import forms

class StudentForm(forms.Form):
    first_name=forms.CharField()
    name=forms.CharField(help_text="input can not be 30")
    email=forms.EmailField()