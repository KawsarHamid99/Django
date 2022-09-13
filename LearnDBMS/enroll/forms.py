import email
from unicodedata import name
from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField()
    first_name=forms.CharField()
    email=forms.EmailField()

class registrationform2(forms.Form):
    name=forms.CharField(min_length=5,max_length=50,error_messages={'required':"Enter Your Name"})
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean_name(self):
        valname=self.cleaned_data["name"]
        if len(valname)<4:
            raise forms.ValidationError("Enter more or 4 char")
        return valname 
