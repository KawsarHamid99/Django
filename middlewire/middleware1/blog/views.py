from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func(request):
    print("this is view page")
    return HttpResponse("Hello World")