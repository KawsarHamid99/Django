from email.headerregistry import Group
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .froms import SignupForm2,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User,Group


def Signup(request):
    if request.method == "POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    return render(request,"UserAuthentication/Registration.html",{'form':fm})


def Signup2(request):
    if request.method=="POST":
        fm=SignupForm2(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name="manager")
            user.groups.add(group)
            messages.success(request,"account create Successfully...!!!")
    else:
        fm=SignupForm2()
    return render(request,"UserAuthentication/Registration.html",{'form':fm})

#username: kawsar111
#password: F1$j2qPjm7At@pc&r

def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data["username"]
                password=fm.cleaned_data["password"]
                user=authenticate(username=username,password=password)
                print("_")
                print(user)
                if user is not None:
                    login(request,user) 
                    messages.success(request,"loggedin successfully...!!")
                    return HttpResponseRedirect("profile")
        else:
            fm=AuthenticationForm()

        return render(request,"UserAuthentication/UserLogin.html",{"form":fm})
    else:
        return HttpResponseRedirect("profile")


"""def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,"Profile Updated")
                fm.save()
        else:
            #fm=UserChangeForm(instance=request.user)
            fm=EditUserProfileForm(instance=request.user)
        return render(request,"UserAuthentication/profile.html",{"name":request.user,"form":fm})
    else:
        return HttpResponseRedirect("login")"""

def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                messages.success(request,"Profile Updated")
                fm.save()
        else:
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                #fm=UserChangeForm(instance=request.user)
                fm=EditUserProfileForm(instance=request.user)
                users=None
        return render(request,"UserAuthentication/profile.html",{"name":request.user,"form":fm,"users":users})
    else:
        return HttpResponseRedirect("login")



def Logout(request):
    logout(request)
    return HttpResponseRedirect("login")

def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                #if you don't use "update_session_auth_hash" this after update this password, you will logged out
                messages.success(request,"password changed successfully...")
                return HttpResponseRedirect("profile")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,"UserAuthentication/changepassword.html",{"form":fm})
    else:
        return HttpResponseRedirect("login")

def changepassWithoutOld(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                #if you don't use "update_session_auth_hash" this after update this password, you will logged out
                messages.success(request,"password changed successfully...")
                return HttpResponseRedirect("profile")
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,"UserAuthentication/chngPasswithoutold.html",{"form":fm})
    else:
        return HttpResponseRedirect("login")


def user_details(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=EditAdminProfileForm(instance=pi)
        return render(request,"UserAuthentication/userDetails.html",{"form":fm})
    else:
        return HttpResponseRedirect("login")


def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,"UserAuthentication/user_dashboard.html",{"name":request.user.username})
    else:
        return HttpResponseRedirect("login")