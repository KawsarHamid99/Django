from django.shortcuts import render
from .models import Studentlist
from django.core.paginator import Paginator
from django.views.generic import TemplateView,View
from django.http import JsonResponse
# Create your views here.
# Studentlist.objects.get_or_create(name="rakib"+str(i),email=str(i)+"rakib@gmail.com",faculty="SCIENCE")

global_list=10
def pagination(request):
    global global_list
    studentlist=Studentlist.objects.all()
    paginator=Paginator(studentlist,global_list)
    page=request.GET.get('page')
    student_list=paginator.get_page(page)
    return render(request,"pagination_1.html",{"student_list":student_list})


class MainView(TemplateView):
    template_name="showmore.html"

class PostJsonListView(View):
    def get(request,*args,**kwargs):
        print(kwargs)
        upper=kwargs.get('num_post')
        lower=upper-3
        posts=list(Studentlist.objects.values()[lower:upper])
        posts_size= len(Studentlist.objects.all())
        size=True if upper >= posts_size else False 

        return JsonResponse({'data':posts,'max':size},safe=False)
