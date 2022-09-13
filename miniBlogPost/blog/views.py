import re
from tokenize import group
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SignupForm,LoginForm,PostForms
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,"blog/home.html",{'posts':posts})

def about(request):
    return render(request,"blog/about.html")

def contact(request):
    return render(request,"blog/contact.html")
# 46t-fM3*@c
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Loggid in Successfully")
                    return HttpResponseRedirect("/dashboard")
            
        else:
            form = LoginForm()
        return render(request,"blog/login.html",{'form':form})
    else:
        return HttpResponseRedirect("/dashboard")

def user_signin(request):
    if request.method =="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name="author")
            user.groups.add(group)
            messages.success(request,"congratulations..!!!")

    else:
        form = SignupForm()
    return render(request,"blog/signup.html",{'form':form})

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        fullname=user.get_full_name()
        gps=user.groups.all()
        return render(request,"blog/dashboard.html",{"posts":posts,"fullname":fullname,"groups":gps})
    else:
        return HttpResponseRedirect("/login")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=PostForms(request.POST)
            if form.is_valid():
                title=form.cleaned_data["title"]
                desc=form.cleaned_data["desc"]
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForms()
        else:
            form=PostForms()
        return render(request,"blog/addpost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login")


def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            form=PostForms(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/dashboard")
        else:
            pi=Post.objects.get(pk=id)
            form=PostForms(instance=pi)
        return render(request,"blog/updatepost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login")

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect("/dashboard")
    else:
        return HttpResponseRedirect("/login")