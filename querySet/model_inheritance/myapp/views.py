from django.shortcuts import render
from .models import St,Teacher,Contractor

# Create your views here.
def base(request):
    student=St.objects.all()
    teacher=Teacher.objects.all()
    contractor=Contractor.objects.all()

    return render(request,"base.html",{"student":student,"teacher":teacher,"contractor":contractor})
