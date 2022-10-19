from django.shortcuts import render

from myapp.forms import StudentForm
from .forms import studentClass
# Create your views here.
def conf(request):
    
    #form=StudentForm(auto_id=True)
    #form=StudentForm(auto_id="some_%s")
    #form=StudentForm(auto_id="kawsar")
    #form=StudentForm(auto_id=True,label_suffix='  :-  ')
    form=StudentForm(label_suffix=':- ',initial={'name':'Kawsar','email':'sonam@gmail.com'},field_order=["email",'name'])
    if request.method=="POST":
        print(request.POST["name"])
        print(request.POST["email"])
    return render(request,"configure_id/base.html",{'form':form})

        