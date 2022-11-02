from django.shortcuts import render,HttpResponse
from .forms import studentRegistration
# Create your views here.

def home(request):
    if request.method=="POST":
        fm=studentRegistration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data["name"])
    


    path="stylingFormError/stylingformerror1.html"
    return render(request,path,{'form':fm})