from django.shortcuts import render
from django.views.generic import View
from .models import student,Teacher
from datetime import date,time
from django.db.models import Avg,Min,Max,Sum
from django.db.models import Q
from datetime import datetime

# Create your views here.
class HomeView(View):
    def get(self,request):
        
        objs=[ 
            Teacher(name="Aftab",empnum=20231,city="Khulna",salary=20555,join_date="2018-8-19"),
            Teacher(name="tamim",empnum=33313,city="costarica",salary=40823,join_date="2022-6-16"),
            Teacher(name="kopila",empnum=40012,city="chompa",salary=15000,join_date="2021-7-3")
        ]

        #stu=Teacher.objects.bulk_create(objs)
        

        data=student.objects.filter(city="chandpur")

        stu=student.objects.order_by("id")
        stu=student.objects.in_bulk()

        print("---------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------")
        print(stu)
        print(datetime.now())
        #for i in stu:
            #print(f"id:{i.id}  name:{i.name}  roll:{i.roll}   city:{i.city}   marks:{i.marks}  pass_date:{i.pass_date}   admitdate:{i.admitdate}")

        return render(request,"modelRelationShip2/home.html")