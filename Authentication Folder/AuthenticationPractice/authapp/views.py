from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .froms import SignupForm,UserProfileUpdate,EditAdminProfile
from django.contrib.auth.models import User,Group

def func(request):
    return render(request,"authapp/home.html")

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            print("----------------------------hoooo----------------")
            print(request.user.username)
            #print(request.user.password)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    print("-------------------------------------")
                    messages.success(request,"login successfully")

                    return HttpResponseRedirect("/profile/") 
        else:
            fm=AuthenticationForm()
        return render(request,"authapp/login.html",{"form":fm})
    else:
        return HttpResponseRedirect("/")


def signup_form(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"signup successfully...!!")
            user=fm.save()

            if Group.objects.filter(name="editors").exists():
                grp=Group.objects.get(name="editors")
                user.groups.add(grp)
                
    else:
        fm=SignupForm()
    return render(request,"authapp/login.html",{'form':fm})

#profile
def user_details(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UserProfileUpdate(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,"Updated successfully")
                fm.save()
        else:
            fm=UserProfileUpdate(instance=request.user)
        return render(request,"authapp/profile.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


def permissionBasesProfile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    else:
        if request.method=="POST":
            if request.user.is_superuser==True:
                fm=EditAdminProfile(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=UserProfileUpdate(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                fm.save()
                messages.success(request,"profile updated")

        else:
            if request.user.is_superuser==True:
                fm=EditAdminProfile(instance=request.user)
                users=User.objects.all()
            else:
                fm=UserProfileUpdate(instance=request.user)
                users=None
        return render(request,"authapp/profile.html",{'form':fm,'users':users})


def user_info(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(id=id)
        fm=EditAdminProfile(instance=pi)
        return render(request,"authapp/profile.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/profile/")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,"authapp/changepass.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")

def set_password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect("/profile/")
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,"authapp/changepass.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/") 

def dashboard(request):
    if request.user.is_authenticated:
        group=Group.objects.all()
        print("--------------------------")
        print(group)

        return render(request,"authapp/dashboard.html",{'name':request.user.username}) 
    else:
        return HttpResponseRedirect("/login/")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/" )

