from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import ContactForm


# Create your views here.


class Myview(View):
    name='bekar pola'
    age=None
    def get(self,request):
        return HttpResponse(self.age)
class HomeClass(View):
    def get(self,request):
        context={'name':'My name is kawsar'}
        return render(request,"base.html",context)


def cf(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print("name:",form.cleaned_data['name'])
            return HttpResponse('<h3>Thanks for submitting...</h3>')
    else:
        form=ContactForm()
        return render(request,"contact.html",{'form':form})


class contactForm(View):
    def get(self,reuqest):
        form=ContactForm()
        return render(reuqest,"contact.html",{'form':form})
    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            print("name: ",form.cleaned_data["name"])
            return HttpResponse("thanks for submitting...")




