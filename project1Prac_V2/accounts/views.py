import email
from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid user or password")
            return redirect("login")
    else:
        return render(request,"login.html")


def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        print(first_name+" "+last_name+" "+username+" "+email+" "+password1+" "+password2)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email has been taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                messages.info(request,"created")
                return redirect("register")

    else:
        return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect("/")

