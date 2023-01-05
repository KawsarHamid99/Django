from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages

def func(request):
    return render(request,"authapp/home.html")

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"login successfully")
                    return HttpResponseRedirect("/")
        else:
            fm=AuthenticationForm()
        return render(request,"authapp/login.html",{"form":fm})
    else:
        return HttpResponseRedirect("/")
        #return render(request,"authapp/home.html")

