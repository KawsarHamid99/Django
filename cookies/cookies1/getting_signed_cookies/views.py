from datetime import datetime,timedelta
from email.mime import base
from django.shortcuts import render


# Create your views here.
def home(request):
    reponse=render(request,"base.html")
    reponse.set_signed_cookie("sname","Kawsar",salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    return reponse

def get_cookies(request):
    name=request.get_signed_cookie('sname',default="None",salt='nm')
    return render(request,"getcookies.html",{"cookies":name})

def del_cookies(request):
    reponse=render(request,"delcookies.html")
    reponse.delete_cookie('sname')
    return reponse