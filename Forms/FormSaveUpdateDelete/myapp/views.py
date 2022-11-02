
from django.shortcuts import render
from .models import StudentModels
from .forms import Student
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=Student(request.POST)
        if fm.is_valid():
            names=fm.cleaned_data.get("name")
            emails=fm.cleaned_data.get("email")
            passwords=fm.cleaned_data.get("password")
            print("------------------------------------------------------")
            print(names)
            print(emails)

            model=StudentModels(name=names,email=emails,password=passwords)
            model.save()

            #update&delete
            #model=StudentModels(id==1)
            #model.save()

            #model.delete()

    else:
        fm=Student()
    return render(request,"base.html",{'form':fm})
