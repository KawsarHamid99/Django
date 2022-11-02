from django import forms

class StudentRegistrationForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField(required=False)