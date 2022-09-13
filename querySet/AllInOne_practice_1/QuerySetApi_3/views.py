from django.shortcuts import render,HttpResponse
from QuerySetApi_1.models import Student
from django.db.models import Q
from django.db.models import Avg,Min,Max,Sum

# Create your views here.
def home(request):
    data2=Student.objects.order_by('id')

    #data=Student.objects.filter(name__iexact='kawsar')
    #data=Student.objects.filter(name__iexact="turin")

    #data=Student.objects.filter(name__contains="K")
    #data=Student.objects.filter(name__icontains="K")

    #data=Student.objects.filter(id__gt=4) & Student.objects.filter(id__lt=12)
    #data=Student.objects.filter(id__gte=4) & Student.objects.filter(id__lte=12)
    #data=Student.objects.filter(id__range=(4,10))

    #data=Student.objects.filter(name__startswith='k')
    #data=Student.objects.filter(name__istartswith='k')

    #data=Student.objects.filter(name__iendswith='n')
    #data=Student.objects.filter(pass_date__range=('2001-08-07','2012-12-12'))
    
    #data=Student.objects.filter(name__icontains='K')
    #data=Student.objects.filter(pass_date__year__gte=2021)
    #data=Student.objects.filter(pass_date__month__gt=5)
    #data=Student.objects.filter(pass_date__month=5)
    #data=Student.objects.filter(pass_date__day__gt=10)
    #data=Student.objects.filter(roll__isnull=False)

    data=Student.objects.all()

    data=Student.objects.filter(Q(id=2) & Q(roll=123))

    data=Student.objects.filter(Q(id=6) | Q(name='kawsar'))

    print(Student.objects.aggregate(Sum('marks'))) 

    return render(request,'queryset_3/home.html',{'student':data,'student2':data2})

