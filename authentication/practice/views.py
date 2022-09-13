from distutils.log import log
import re
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib import messages
from .forms import signUp_form,EditUserM

from django.contrib.auth import login,logout,authenticate,update_session_auth_hash


def home(request):
    if request.method=="POST":
        fm=signUp_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"account create successfully...!!!")
            fm=signUp_form()
    else:
        fm=signUp_form()  
    return render(request,"practice/auth.html",{"form":fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                passw=fm.cleaned_data["password"]
                user=authenticate(username=uname,password=passw)

                if user is not None:
                    login(request,user)
                    messages.success(request,"logged in successfully...!!!")
                    return HttpResponseRedirect("/practice/profile")
        else:
            fm=AuthenticationForm()
        return render(request,"practice/login.html",{"form":fm})
    else:
        return HttpResponseRedirect("/practice/profile")



def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=EditUserM(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"updated...")
                return HttpResponseRedirect("/practice/profile")
        else:
            fm=EditUserM(instance=request.user)
        return render(request,"practice/profile.html",{"name":request.user,"form":fm})
    else:
        return HttpResponseRedirect("/practice/login")



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/practice/login")
    else:    
        return HttpResponseRedirect("/practice/login")

def passwordChangeWithOld(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                messages.success(request,"password updated...")
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/practice/profile")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,"practice/passwordChange.html",{"form":fm})
    else:
        return HttpResponseRedirect("/practice/login")


def passwordChangeWithoutold(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"password updated successfully....")
                return HttpResponseRedirect("/practice/profile")
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,"practice/passwordChange.html",{"form":fm})
    else:
        return HttpResponseRedirect("practice/profile")

