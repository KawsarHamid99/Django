from unicodedata import name
from django.shortcuts import render
from QuerySetApi_1.models import Student
# Create your views here.

def home(request):
    data=Student.objects.earliest("pass_date")
    print(Student.objects.all().exists())
    sdata=Student.objects.all()

    one_data=Student.objects.get(pk=1)
    print(sdata.filter(pk=one_data.pk).exists())
    #data=Student.objects.create(name='Turin',roll=2111,dept='Physics',marks=60,pass_date='2020-06-07')
    #data,created=Student.objects.get_or_create(name='Israt',roll=3223,dept="Chemistry",marks=80,pass_date='2021-05-08')
    #data=Student.objects.filter(roll=233).update(dept='CSE')
    #data,created=Student.objects.update_or_create(id=2,name="babu",defaults={'name':"sakib",'roll':123,'dept':"EEE",'marks':80,'pass_date':'2021-05-08'})
    #data,created=Student.objects.update_or_create(id=3,defaults={'name':'Turin','roll':133,'dept':'CSE','marks':99,'pass_date':'2021-05-08'})

    



    obj=[ 
        Student(name='kawsar',roll=12032,dept='LLB',marks=88,pass_date='2001-08-07'),
        Student(name='Rakhi',roll=14503,dept="CSE",marks=77,pass_date='2012-02-24'),

    ]
    #data=Student.objects.bulk_create(obj)

    all_student=Student.objects.filter(name='kawsar')
    for stu in all_student:
        stu.marks=99

    #data=Student.objects.bulk_update(all_student,['marks'])
    #data=Student.objects.bulk_update(all_student,['marks'])
    data=Student.objects.get(pk=17).delete()

    print("--------------------------------------------------------------------------------------")
    #data=Student.objects.in_bulk([1,2])
    print(data[1])
    





    
    print(obj)

    return render(request,"queryset_2/base.html",{'student':one_data})
