from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import forms,Registration
from django.views.generic.base import TemplateView
# Create your views here.

class  registration(View):
    def get(self,request):
        form=Registration()
        return render(request,"registration.html",{'forms':form})
    def post(self,request):
        form=Registration(request.POST)
        if form.is_valid():
            print("name: ",form.cleaned_data['name'])
            return HttpResponse("<h1> thanks for submitting </h1>")


class inform(View):
    name='kawsar'
    age=None
    def get(self,request):
        return HttpResponse(self.name)


class HomeView(TemplateView):
    template_name="home.html" 

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sonam'
        context['roll']=101
        print("----------------------------------------------")
        print(kwargs)

        return context


class contactView(TemplateView):
    template_name='home.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["name"]='bakis'
        context['roll']=200
        print(kwargs)
        return context

class xview(TemplateView):
    template_name='home.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sonam'
        return context





        

    



