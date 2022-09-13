from turtle import update
from unicodedata import name
from venv import create
from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    #student_data=Student.objects.get(pk=4)
    #student_data=Student.objects.first()
    #student_data=Student.objects.order_by("name").first()
    #student_data=Student.objects.order_by("name").last()
    #student_data=Student.objects.latest("pass_date")
    #student_data=Student.objects.earliest("pass_date")

    #student_data=Student.objects.all()
    #print(student_data.exists())
    #one_data=Student.objects.get(pk=1)
    #print(student_data.filter(pk=one_data.pk).exists())

    #student_data=Student.objects.create(name="abdul",roll=132,city="Badda",marks=89,pass_date='2022-1-5')
    #student_data,created=Student.objects.get_or_create(name="sabbir",roll=133,city="pabna",marks=91,pass_date="2021-1-7")
    #student_data=Student.objects.filter(roll=132).update(city="badda",marks=99)
    #student_data=Student.objects.filter(city="dhaka").update(marks=90)
    #student_data,created=Student.objects.update_or_create(id=12,name="hazrat",defaults={'name':"hazrat",'roll':151,'marks':89,'pass_date':'2020-5-7'})

    '''
    objs=[
        Student(name="Aftab",roll=155,city='Chandpur',marks=90,pass_date='2021-5-7'),
        Student(name="Aftab",roll=156,city='Chandpur',marks=95,pass_date='2021-5-7'),
        Student(name="Aftab",roll=157,city='Cumilla',marks=99,pass_date='2022-7-9'),
        Student(name="Aftab",roll=158,city='Cumilla',marks=90,pass_date='2022-7-9'),
    ]
    student_data=Student.objects.bulk_create(objs)
    '''


    '''
    all_student_data=Student.objects.filter(city="chandpur")
    for stu in all_student_data:
        stu.marks=88
    student_data=Student.objects.bulk_update(all_student_data,['marks'])
    '''

    #student_data=Student.objects.in_bulk([1,2])
    #print(student_data[2].name)
    #student_data=Student.objects.in_bulk()


    #student_data=Student.objects.all().delete()
    #student_data=Student.objects.get(pk=12).delete()
    #student_data=Student.objects.filter(marks=255).delete()
    student_data=Student.objects.all()
    print(student_data.count())













    print("-----------------------------------------------------------------------")
    print("Return: ",student_data )
    #print("Return: ",created )
    print("")
    #print("Query: ",student_data.query)
    print("-----------------------------------------------------------------------")
    return render(request,"base.html",{"student":student_data})