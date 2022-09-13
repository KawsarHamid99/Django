from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello World") 

def excp(request):
    print("i am excp view")
    a=10/0
    return HttpResponse("Hello Excp view")


def user_info(request):
    print("user info view")
    context={"name":"Rahul"}
    return TemplateResponse(request,"context.html",context)
