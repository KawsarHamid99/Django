from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            #fm.save()
            name=fm.cleaned_data.get('name')
            email=fm.cleaned_data.get('email')
            dept=fm.cleaned_data.get('dept')
            password=fm.cleaned_data.get('password')

            reg=Student(name=name,email=email,dept=dept,password=password)
            reg.save()
    else:
        fm=StudentForm()
    return render(request,"ModelForm/base.html",{"form":fm})