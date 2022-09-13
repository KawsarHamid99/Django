from django.shortcuts import render
from account.forms import RegistrationForm
from django.http import HttpResponse


#For login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return HttpResponse("you are authenticated")
    else:
        form=RegistrationForm()
        if request.method=="post" or request.method=='POST':
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("your account is valid")
    context={
        'form':form
    }
    return render(request,'register.html',context)

def login(request):
    if request.user.is_authenticated:
        return HttpResponse("you are alrady logged in")
    else:
        if request.method=="post" or request.method=='POST':
            username=request.POST.get("username")
            password=request.POST.get("password")
            customer=auth.authenticate(username=username,password=password)
            if customer is not None:
                print("____________"+customer.password+"________________")
                auth.login(request,customer)
                return HttpResponse("you are login successfully")
            else:
                return HttpResponse("username or passowrd is incorrect")
                
    return render(request,"login.html")
