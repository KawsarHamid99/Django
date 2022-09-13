from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from enroll.forms import studentRegistration,registrationform2

from enroll.models import Student
# Create your views here.

def home(request):
    stud= Student.objects.all()
    return render(request,"enroll/studetails.html",{"stu":stud})


def stuForm(request):
    #form=studentRegistration()
    #form=studentRegistration(auto_id='some_%s')
    #form=studentRegistration(auto_id=True)
    #form=studentRegistration(auto_id=False)
    #form=studentRegistration(auto_id='geeky')
    #form=studentRegistration(auto_id='geeky', label_suffix=":   ")
    #form=studentRegistration(auto_id='geeky', label_suffix=":   ",initial={'name':'kawsar','email':'kawsar@gmail.com'})
    form=studentRegistration()
    form.order_fields(field_order=['first_name',"name","email"])
    return render(request,"enroll/Form.html",{"form":form})


def form2(request):
    if request.method=="POST":
        form=registrationform2(request.POST)
        if form.is_valid()==True:
            print(form.is_valid())
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            print("Name: ",name)
            print("Email: ",email)  
            print("password : ",password)
 
            return redirect("forms2")
        else:
            return redirect("forms2")

    else:
        form=registrationform2()
        return render(request,"enroll/form2.html",{"form":form})


