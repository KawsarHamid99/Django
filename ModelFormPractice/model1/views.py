from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import students
# Create your views here.

def home(request):
    stud=students.objects.all()
    stx=students.objects.get(pk=2)
    return render(request,'model1/base.html',{"stu":stud,"stx":stx})
