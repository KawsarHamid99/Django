from django import forms
from .models import Registration


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['student_name','email','age','depertment']


class TeacherRegistrationForm(StudentRegistrationForm):
    class Meta(StudentRegistrationForm.Meta):
        fields=['teacher_name','email','age','depertment']
        #exclude=["student_name"]
        
        