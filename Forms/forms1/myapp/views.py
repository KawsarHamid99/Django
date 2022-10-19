from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    if request.method=="POST":
        form=StudentForm(label_suffix="  :- ",auto_id="geeky_%s",field_order=['email','name'])
        print(request.POST["name"])
        print(request.POST["email"])
        return render(request,"form1/base.html",{'form':form})
    else:
        form=StudentForm(label_suffix=":_",initial={"name":'kawsar','email':'kawsar@gmail.com'})
        return render(request,"form1/base.html",{'form':form})
