from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta

# Create your views here.

def home(request):
    response=render(request,"base.html")
    #response.set_cookie("name","sonam",max_age=40)
    response.set_cookie("name","sonam",expires=datetime.utcnow()+timedelta(days=2))
    return response


def getcookies(request):
    #name=request.COOKIES['name']
    #name=request.COOKIES.get("name")
    name=request.COOKIES.get("name","default")
    return render(request,"getcookies.html",{"cookies":name})


def delcookies(request):
    reponse=render(request,"delcookies.html")
    reponse.delete_cookie('name')
    return reponse
