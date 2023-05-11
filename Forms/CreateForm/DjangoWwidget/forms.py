import email
from unicodedata import name
from django import forms

Birth_yearChoice=['1099','2000','2001']
Clr_choice=[ 
    ('red','Red'),
    ('green','Green'),
    ('black',"Black")
]
 


class StudentForm(forms.Form):
    name=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','id':'uniqueid'}))
    email=forms.EmailField(required=False,disabled=True,initial="kasar@gmail.com", label_suffix=" :-: ")
    fav_clr=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple(choices=Clr_choice))



    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=Birth_yearChoice))
    description=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))