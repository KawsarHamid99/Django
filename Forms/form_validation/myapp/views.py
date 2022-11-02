from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import StudentRegistrationForm


def success(request):
    return render(request,"success.html")


def showFormData(request):
    #fm=StudentRegistrationForm()
    #fm=StudentRegistrationForm(auto_id='some_%s')
    
    if request.method=="POST":
        fm=StudentRegistrationForm(request.POST)
        print(fm)
        print("Form POst request")
        if fm.is_valid():
            print(fm.cleaned_data)
            print(fm.cleaned_data["name"])
            print(request.POST["name"])
            return HttpResponseRedirect("success/")
    else:
        fm=StudentRegistrationForm()
        print("Form Get Request")
    return render(request,"base.html",{'form':fm})