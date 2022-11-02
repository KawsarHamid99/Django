
from asyncio import FIRST_COMPLETED
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from  .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.  

def home(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm=UserCreationForm()
    return render(request,"auth/base.html",{'form':fm})

# SignUP
def SignupForms(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Signup successfully")
            fm.save()

    else:
        fm=SignupForm()
    return render(request,"auth/signup.html",{'form':fm})

# Login View

def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(username=uname,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"login successfully")
                    return HttpResponseRedirect("/profile/")
        else:
            fm=AuthenticationForm()

        return render(request,"auth/login.html",{'form':fm})
    else:
        return HttpResponseRedirect("/profile/")

# Profile
def details(request):
    if request.user.is_authenticated:
        return render(request,"auth/profile.html",{'name':request.user})
    else:
        return HttpResponseRedirect("/login/")


#logout
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login/")