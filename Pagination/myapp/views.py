from django.shortcuts import render
from .models import Studentlist
from django.core.paginator import Paginator
# Create your views here.
# Studentlist.objects.get_or_create(name="rakib"+str(i),email=str(i)+"rakib@gmail.com",faculty="SCIENCE")

global_list=10
def home(request):
    global global_list
    studentlist=Studentlist.objects.all()
    paginator=Paginator(studentlist,global_list)
    page=request.GET.get('page')
    student_list=paginator.get_page(page)
    return render(request,"pagination_1.html",{"student_list":student_list})