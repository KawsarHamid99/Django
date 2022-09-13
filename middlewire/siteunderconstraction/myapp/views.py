from urllib import request
from django.shortcuts import render

# Create your views here.
def home(request):
    print("i am home page")
    return render(request,"base.html")


def about(request):
    print("hello from about page")
    return render(request,"about.html")