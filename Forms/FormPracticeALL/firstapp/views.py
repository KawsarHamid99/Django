from django.shortcuts import render
# Create your views here.
from .forms import StudentForms,StudentInherit
def Home(request):
    if request.method=="POST":
        print("-------------------------")
        fm=StudentInherit(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data["password"])
        return render(request,"firstapp/base.html",{'form':fm})
    else:
        fm=StudentInherit()
        return render(request,"firstapp/base.html",{"form":fm})
