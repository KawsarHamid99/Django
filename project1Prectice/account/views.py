import email
from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print("________________________success_________________")
            auth.login(request,user)
            print("________________________ succcess-2_________________")
            return redirect("/")

        else:
            messages.info(request,"invalid credentials")
            print("________________________invalid credentials_________________")
            return redirect("login")
    else:
        print("________________________Hello Peter_________________")
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        #user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        #user.save()
        print(first_name+" "+last_name+" "+username+" "+email+" "+password1+" "+password2)
        
        #return redirect("register")
        #'''
        if password1==password2:
            print("_____________1______________")
            if User.objects.filter(username=username).exists():
                print("_____________2______________")
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("_____________3______________")
                messages.info(request,"email has been used")
                return redirect('register')
            else:
                print("_____________4______________")
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                messages.info(request,"Created")
                return redirect('login')    
                #'''
        else:
            print("password is not matching")
    else:
        print("hello")
        print("_____________5______________")
        return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect("/")