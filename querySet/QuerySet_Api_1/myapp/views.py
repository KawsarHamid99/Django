from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

###   QuerySet API Method That Return New Query Set
def home(request):
    #data=Student.objects.all()
    #data=Student.objects.filter(marks=55)
    #data=Student.objects.exclude(marks=55)
    #data=Student.objects.order_by("-city")
    #data=Student.objects.order_by("city")
    #data=Student.objects.order_by("?")
    #data=Student.objects.order_by("city").reverse()[0:3]
    #data=Student.objects.values()
    #data=Student.objects.values("name","city")
    #data=Student.objects.distinct()
    #data=Student.objects.values_list()
    #data=Student.objects.values_list("id","name")
    #data=Student.objects.values_list("id","name",named=True)
    #data=Student.objects.using("default")
    #data=Student.objects.dates('pass_date',"month")
    #data=Student.objects.dates('pass_date',"year")

    #######################  second tables "Teacher"  #########################

    qs1=Student.objects.values_list('id','name',named=True)
    qs2=Teacher.objects.values_list('id','name',named=True)
    #data=qs2.union(qs1)
    #data=qs2.union(qs1,all=True)
    #data=qs2.intersection(qs1)
    data=qs1.difference(qs2)


    ###################### And Or Operator ###############################

    #data=Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    #data=Student.objects.filter(id=6,roll=106)

    data=Student.objects.filter(id=16) | Student.objects.filter(roll=106)
    #data=Student.objects.filter( Q(id=6) | Q(roll=106)  )   #This is not working ,i dont know why
    



    print("---------------------------------------------------------------------------------")
    print("Return:",data)
    print("")
    print("Query",data.query)
    print("-----------------------------------------------------------------------------------")
    return render(request,"home.html",{"students_data":data})
