from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def reg(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"Your Account Has ben created !!! ")
            messages.info(request,"now you can login")      
            print(messages.get_level(request))
            messages.debug(request,"hello from debug")
            print(f"---------------------{messages.get_level(request)}")

            messages.set_level(request,messages.DEBUG)
            messages.debug(request,"hello from NEW debug")
            print(messages.get_level(request))


            messages.error(request,"This is error ")

    else:
        fm=StudentRegistration()
    return render(request,"MessagesFramework/userRegistration.html",{'form':fm})


