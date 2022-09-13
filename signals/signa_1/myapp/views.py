from django.shortcuts import render

def home(request):
    return render(request,"signal1/home.html")