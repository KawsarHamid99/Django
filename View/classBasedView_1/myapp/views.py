from multiprocessing import context
from django.shortcuts import render
from django.views import View
from .forms import Contactform
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello World")


#Class based view
class myview(View):
    name='baker'
    def get(self,request):
        #return HttpResponse("Class Based View")
        return HttpResponse(self.name)

class childclass(myview):
    def get(self, request):
        return HttpResponse(self.name)


class HomeClassView(View):
    
    def get(self,request):
        context={'msg':"welcome to kawsar hamid's show "}
        return render(request,"home.html",context)


def contactfun(request):
    if request.method=='POST':
        form=Contactform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("<h3>Thanks For Submit...</h3>")
    else:
        form=Contactform()
    return render(request,'contact.html',{'form':form})


class ContactClassView(View):
    def get(self,request):
        form=Contactform()
        return render(request,"contact.html",{'form':form})
    def post(self,request):
        form=Contactform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thanks For Submit...') 
            






