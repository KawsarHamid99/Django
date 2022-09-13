from email.policy import default
from tkinter.tix import Tree
from unicodedata import name
from django.shortcuts import render
from .models import Student, Teacher
def home(request):

    data=Student.objects.dates('pass_date','month')
    qs1=Student.objects.values_list('id','name',named=True)
    qs2=Teacher.objects.values_list('id','name',named=True)

    data=qs1.union(qs2)
    data=qs1.union(qs2,all=True)

    data=Student.objects.filter(name="kawsar") & Student.objects.filter(roll=308316)
    data=Student.objects.dates('pass_date','year')


    print("----------------------------------------------------------------------------------------")
    #print(qs1)
    print("")
    #print(qs2)
    print("")
    print(data)
    print("")
    print(type(data))
    print("")
    print(data.query)
    print("----------------------------------------------------------------------------------------")

    return render(request,"queryset_1/home.html",{"student":data})

