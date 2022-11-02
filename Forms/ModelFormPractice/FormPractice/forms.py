
from django import forms
from django.core import validators


class StudentRegistration(forms.Form):
    name=forms.CharField(strip=False,min_length=5,widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'kawsar@gmail.com','value':"phk@gmail.com"})) 
    dept=forms.CharField(empty_value="pakis",label="Depertment")
    price=forms.DecimalField(max_digits=4,decimal_places=2,error_messages={'required':'can not be empty',"max_digits":"max length should be 4","decimal_places":"decimal piont 2"})

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



def start_with_k(value):
    if value[0] != "k":
        raise forms.ValidationError("Should be Start with k")

def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError(' Should be start with s') 

clr=[ 
    ('red','Red'),
    ('green','green'),
    ('yellow',"yellow"),
]

birth_yr=[ 
    '1999','2000','2001','2002'
]

class Registration2(forms.Form):
    name=forms.CharField(validators=[start_with_k])
    dept=forms.CharField(validators=[validators.MaxLengthValidator(5)])
    group=forms.CharField()
    fav_clr=forms.MultipleChoiceField(required=False,choices=clr,widget=forms.CheckboxSelectMultiple)
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=birth_yr))
    email=forms.EmailField()

    '''
    def clean_group(self):
        valgrp=self.cleaned_data["group"]
        if len(valgrp) > 5:
            raise forms.ValidationError("group lenght should be less then 5")
    '''
    def clean(self):
        cleaned_data=super().clean()
        valgrp=self.cleaned_data["group"]
        print(valgrp)
        if len(valgrp) > 5:
            raise forms.ValidationError("Lenght > 5")

