from django.shortcuts import render
from .forms import StudentRegistration,Registration2
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data.get("name")
            dept=fm.cleaned_data.get("dept")
            email=request.POST["email"]
            print(f"name:{name}      email:{email}     dept: {dept}")
    else:
        fm=StudentRegistration()
    return render(request,"Form/base.html",{'form':fm})


def registration2(request):
    if request.method=="POST":
        fm=Registration2(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=request.POST["email"]
            print(f"name:{name}      email:{email}")
    else:
        fm=Registration2()
    return render(request,"Form/base.html",{'form':fm})