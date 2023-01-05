from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from .forms import UserRegistrationForm,EditAdminForm,EditUserForm
from django.contrib.auth.models import User,Group
from django.contrib import messages

from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
# Create your views here.



def User_Registration(request):
    if request.method=="POST":
        fm=UserRegistrationForm(request.POST)
        if fm.is_valid():
            if Group.objects.filter(name="Editors").exists():
                user=fm.save()
                group=Group.objects.get(name="Editors")
                user.groups.add(group)
            else:
                fm.save()
            fm=UserRegistrationForm()

            messages.success(request,"User Creates Successfully...")

    else:
        fm=UserRegistrationForm()
    return render(request,"myadmin/registration.html",{'form':fm})



def User_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                password=fm.cleaned_data['password']
                user=authenticate(username=uname,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"User Login Successfully...")

                    return HttpResponseRedirect("/profile/")

        else:
            fm=AuthenticationForm()
        return render(request,"myadmin/login.html",{'form':fm})
    else:
        return HttpResponseRedirect("/profile/")

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser:
                fm=EditAdminForm(request.POST,instance=request.user)
                userlist=User.objects.all()
            else:
                fm=EditUserForm(request.POST,instance=request.user)
                userlist=None
            if fm.is_valid():
                fm.save()
                messages.success(request,"User Updated Successfully...")
        else:
            if request.user.is_superuser:
                fm=EditAdminForm(instance=request.user)
                userlist=User.objects.all()
            else:
                fm=EditUserForm(instance=request.user)
                userlist=None
        return render(request,"myadmin/profile.html",{"form":fm,'users':userlist})
    else:
        HttpResponseRedirect("")


def user_passwordChange(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password updated successfully")
                return HttpResponseRedirect("/profile/")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,"myadmin/changepass.html",{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def edit_user(request,id):
    if request.user.is_authenticated:
        
        if request.method=="POST":
            pi=User.objects.get(pk=id)
            fm=EditAdminForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,"User Updated Successfully...")
        else:
            pi=User.objects.get(pk=id)
            fm=EditAdminForm(instance=pi)
               
        return render(request,"myadmin/profile.html",{"form":fm})
    else:
        HttpResponseRedirect("")


def set_userpassowrd(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"passowrd has been set successfully...")
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/profile/")
        else:
            fm=SetPasswordForm(user=request.POST)
        return render(request,"myadmin/changepass.html",{'form':fm})
    return HttpResponseRedirect("/login/")
    
def permission_dashboard(request):
    data=Group.objects.all()
    print("-------------------")
    print(data)
    print(request.user.groups)
    print(request.user.username)
    return render(request,"myadmin/dashboard.html",{"name":request.user.username})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")
