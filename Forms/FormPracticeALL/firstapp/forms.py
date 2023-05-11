from django import forms
from django.core import validators
from .models import StudentModel


class StudentForms(forms.ModelForm):
    password=forms.CharField(required=True,widget=forms.PasswordInput)
    class Meta:
        model=StudentModel
        fields=["name",'email','password']
        labels={'name':'Name','email':'Email','password':'Password'}
        help_text={'name':'Enter toyr Name'}
        error_messages={'name':{'required':'Enter Your Name'},'email':{'required':'Enter Your Email'}}

        widgets={
            'password':forms.PasswordInput(attrs={'rows':'form-group'}),
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name'})
        }


class StudentInherit(StudentForms):
    class Meta(StudentForms.Meta):
        exclude=["name"]
    



