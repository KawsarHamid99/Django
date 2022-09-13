import email
import re
from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from .forms import studentRegistration

from .models import User

# Create your views here.

def Home(request):
    if request.method=="POST":
        fm=studentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            em=fm.cleaned_data["email"]
            pw=fm.cleaned_data["password"]
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=studentRegistration()

    else:
        fm=studentRegistration()
    stud=User.objects.all()
    return render(request,"addandshow.html",{"form":fm,"stu":stud})


def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


def update_data(request,id):
    if request.method =="POST":
        pi=User.objects.get(pk=id)
        fm=studentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=studentRegistration(instance=pi)

    return render(request,"updatestudents.html",{"form":fm})