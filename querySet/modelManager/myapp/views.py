from urllib import request
from django.shortcuts import render
from .models import Student,Proxystudent
# Create your views here.

def home(request):
    #data=Student.students.all()
    #data=Student.stu.get_stu_roll_range(100,108317)
    data=Proxystudent.proxymanager.get_stu_roll_range(100,108317)

    return render(request,"base.html",{"student":data})
