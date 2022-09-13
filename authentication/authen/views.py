from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User

def home(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"user create successfully...!!!!!!")
            fm=SignUpForm()
    else:
        fm=SignUpForm()
    return render(request,"home.html",{"form":fm})

def user_Login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                unam=fm.cleaned_data["username"]
                upaw=fm.cleaned_data["password"]
                user=authenticate(username=unam,password=upaw)
                if user is not None:
                    login(request,user)
                    messages.success(request,"loged in successfully...!!!")
                    return HttpResponseRedirect("/profile")
        else:
            fm=AuthenticationForm()
        return render(request,"loginForm.html",{"form":fm})
        
    else:
        return HttpResponseRedirect("/profile")

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser:
                fm=EditAdminProfileForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                fm.save()
                messages.success(request,"updated successfully...")
        else:
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(instance=request.user)
                users=None
        return render(request,"profile.html",{"name":request.user,"form":fm,"user":users})
    else:
        return HttpResponseRedirect("/login")

def user_logout(requst):
    logout(requst)
    return HttpResponseRedirect("/login")



def user_changePassword(request):
    if request.user.is_authenticated:

        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/profile")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,"changePassword.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login")



def user_changePassword_withoutold(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/profile")
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,"changePassword.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login")


def user_details(request,id):
    if request.user.is_authenticated: 
        pi=User.objects.get(pk=id)
        fm=EditUserProfileForm(instance=pi)
    return render(request,"userdetails.html",{"form":fm})
