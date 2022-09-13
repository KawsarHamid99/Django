from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    ans1=request.POST["num1"]
    ans2=request.POST["num2"]
    ans=int(ans1)+int(ans2)
    messages.info(request,ans)
    return redirect("home")
