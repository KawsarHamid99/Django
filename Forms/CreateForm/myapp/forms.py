

from django import forms
from django.core import validators
class StudentRegistrationForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()


class MoreOnForm(forms.Form):
    name=forms.CharField(min_length=5,error_messages={'required':"Enter you name"})
    withSpaceValue=forms.CharField(strip=False) #it will accept the value includeing space 
    dept=forms.CharField(max_length=7,empty_value="bakis") #if you dont input any value by default  it will take "bakis"
    agree=forms.BooleanField(error_messages={'required':'you have agree with me'})
    #error_messages=required,max_value,min_value,invalid

    roll=forms.IntegerField(min_value=5,max_value=9)
    price=forms.DecimalField(max_digits=4,decimal_places=1)
    # max_digits=total number of digits, decimal_places=number of digits after decimal point.

    Comment=forms.SlugField()
    description=forms.CharField(widget=forms.Textarea)
    notes=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))


def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError(' Should be start with s') 

class RegForm(forms.Form):
    name =forms.CharField()
    dept=forms.CharField(validators=[validators.MaxLengthValidator(10)])
    group=forms.CharField(validators=[start_with_s])
    email=forms.EmailField()

    # here we validate single object
    '''def clean_name(self):
        valname=self.cleaned_data.get("name")
        #valname=self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('Enter More then or equal 4 Character')
        elif len(valname)>10:
            raise forms.ValidationError("Input must be less then 10")
        return valname

    def clean_email(self):
        valeamil=self.cleaned_data.get('email')
        if len(valeamil)>15:
            raise forms.ValidationError("Email Must contain less then 15 char")'''

    # also we can validate multiple attribute at a time
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data["name"]
        valemail=self.cleaned_data["email"]
        if len(valname)<4:
            raise forms.ValidationError("Enter More then or equal 4 Character")

        if len(valemail)>15:
            raise forms.ValidationError("email must be contain less then 4 Character")

class PasswordValidation(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(label="Password (again )" ,widget=forms.PasswordInput)


    def clean(self):
        cleaned_data=super().clean()
        valpass=self.cleaned_data.get("password")
        valpass2=self.cleaned_data.get("password2")

        if valpass != valpass2:
            raise forms.ValidationError("Password does not match")


