from re import U
import re
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import User
# Create your views here.
def home(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            #nm=request.POST["name"]
            #em=request.POST["email"]
            #pw=request.POST["password"]
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,"crud/addandshow.html",{'form':fm,'stu':stud})

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crud')
def update_data(request,id):
    if request.method == "POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi=User.objects.get(pk=id)
            fm=StudentRegistration(instance=pi)
    return render(request,"crud/updatestudents.html",{'form':fm})

