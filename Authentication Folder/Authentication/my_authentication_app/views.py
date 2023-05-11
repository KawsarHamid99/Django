
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm,UserChangeForm

from  .forms import SignupForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.  


#UserCreationForm
def home(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Account Create Succssfully ")

    else:
        fm=UserCreationForm()
    return render(request,"auth/base.html",{'form':fm})

# SignUP
def SignupForms(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Signup successfully")
            
            if Group.objects.filter(name="Editiors").exists():
                user=fm.save()
                group=Group.objects.get(name="Editiors")
                user.groups.add(group)

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
        if request.method=="POST":
            #
            #show and update the user data
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,"Profile updated")
                fm.save()
        else:
            #show the user data
            fm=EditUserProfileForm(instance=request.user)
        #return render(request,"auth/profile.html",{'name':request.user})
        return render(request,"auth/profile.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


#logout
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login/")

#Change password with old password
def user_changepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"password updated successfully...")
                return HttpResponseRedirect("/profile/")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,"auth/changepassword.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login/")


#Change password without old password
def user_changepass_without_old(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"password updated successfully...")
                return HttpResponseRedirect("/profile/")
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,"auth/changepassword.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login/")


# User view will be shown to user and admin view will be shown to admin.
def Permission_Based_Profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                fm.save()
                messages.success(request,"profile updated...")
        else:
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(instance=request.user)
                users=None
        return render(request,"auth/profile.html",{'form':fm,"users":users})
    else:
        return HttpResponseRedirect("/login/")


def user_details(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=EditAdminProfileForm(instance=pi)
        return render(request,"auth/userdetails.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login/")



def dashboard(request):
    if request.user.is_authenticated:

        group=Group.objects.all()
        print("--------------------------")
        print(group)
        for i in group:
            print(i)
        g=Group.objects.filter(name="lol").exists()
        print(g)
        return render(request,"auth/dashboard.html",{'name':request.user.username})
    else:
        return HttpResponseRedirect("/login/")