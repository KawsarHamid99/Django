from django import forms

class StudentRegistrationForm(forms.Form):
    name=forms.CharField(help_text="must me bore thn 30 char")
    email=forms.EmailField()
    dept=forms.CharField(widget=forms.HiddenInput())


class TeacherRegistrationForm(forms.Form):
    name=forms.CharField(label='Your Name',label_suffix=" :-:", required=False ) 
    dept=forms.CharField(label='Enter your Depertment',label_suffix=":-:",initial="CSE",disabled=True,
    help_text="your dept. ",required=False)
