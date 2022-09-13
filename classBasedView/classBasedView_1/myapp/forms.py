from django import forms

class Contactform(forms.Form):
    name=forms.CharField(max_length=70)