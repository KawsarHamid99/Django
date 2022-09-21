from django import forms

class Registration(forms.Form):
    name=forms.CharField(max_length=100)