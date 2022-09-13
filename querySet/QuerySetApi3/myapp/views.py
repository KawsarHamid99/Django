from enum import unique
from unicodedata import name
from venv import create
from django.shortcuts import render
from .models import student,Teacher
from datetime import date,time
from django.db.models import Q 
from django.db.models import Avg,Sum,Min,Max

# Create your views here.
def home(request):
    #data=student.objects.all()
    #data=student.objects.filter(name__exact='Kawsar')
    #data=student.objects.filter(name__iexact='Kawsar')
    #data=student.objects.filter(name__icontains='T')
    #data=student.objects.filter(name__icontains='U')
    #data=student.objects.filter(id__in=[1,3])
    #data=student.objects.filter(marks__in=[60,99])
    #data=student.objects.filter(marks__gt=90)
    #data=student.objects.filter(marks__gte=90)
    #data=student.objects.filter(marks__lt=90)
    #data=student.objects.filter(marks__lte=90)
    #data=student.objects.filter(name__startswith='T')
    #data=student.objects.filter(name__istartswith='T')
    #data=student.objects.filter(name__endswith='r')
    #data=student.objects.filter(pass_date__range=('2020-04-01','2020-11-05')) #yy-mm-dd
    #data=student.objects.filter(marks__range=(90,99))
    #data=student.objects.filter(admitdate__date=date(2021,7,15))# its works only for models.DateTimeField() function
    #data=student.objects.filter(admitdate__date__gt=date(2021,7,15)) 
    #data=student.objects.filter(pass_date__year=2020)
    #data=student.objects.filter(pass_date__year__gt=2020)
    #data=student.objects.filter(pass_date__year__gte=2020)
    #data=student.objects.filter(pass_date__month=7)
    #data=student.objects.filter(pass_date__year__gte=2020)
    #data=student.objects.filter(pass_date__day=30)
    #data=student.objects.filter(pass_date__week__gt=1)
    #data=student.objects.filter(pass_date__week_day__gt=1)
    #data=student.objects.filter(pass_date__quarter=1)
    #data=student.objects.filter(admitdate__time__gt=time(16,17))
    #data=student.objects.filter(admitdate__hour__gt=16)
    #data=student.objects.filter(admitdate__minute__gte=1)
    #data=student.objects.filter(roll__isnull=True)
    data=student.objects.filter(roll__isnull=False)
    data=student.objects.all()


    # Q Objects
    #data=student.objects.filter(Q(id=3) & Q(roll=1316))
    #data=student.objects.filter(Q(id=3) | Q(roll=2222))
    #data=student.objects.filter(~Q(id=3))
    
    
    #Aggregation
    avg=student.objects.aggregate(Avg('marks'))
    min=student.objects.aggregate(Min('marks'))
    max=student.objects.aggregate(Max('marks'))
    sum=student.objects.aggregate(Sum('marks'))

    print("--------------------------------------------------------------------------------------------------")
    print("")
    print("Average:",avg)
    print("Average:",avg["marks__avg"])
    print("Minimum:",min)
    print("Maximum:",max)
    print("Total:",sum["marks__sum"])

    
    print("")
    print("Return: ",data)
    print("")
    print(student.objects.all().count())
    print("Query:  ",data.query)


    #print(create)
    print("-----------------------------------------------------------------------------------------------")
    return render(request,"base.html",{'student':data})