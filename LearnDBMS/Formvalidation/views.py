from unicodedata import name
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from .forms import ContactForm
from .models import User

def FormCleanAndValidating(request):
    if request.method=="POST":
        fm=ContactForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            em=fm.cleaned_data["email"]
            pw=fm.cleaned_data["password"]
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            print("_________________________________________________Valid____________________ ")
            print(nm)
            print(em)
            print(pw)
            return HttpResponseRedirect("FormCAV")
        else:
            print("________________________________________NOT Valid____________________ ")
            return redirect("FormCAV")
    else:
        form=ContactForm()
        return render(request,"Formvalidation/home.html",{'form':form})

