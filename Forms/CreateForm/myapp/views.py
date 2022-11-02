from django.shortcuts import render

# Create your views here.
from .forms import StudentRegistrationForm,MoreOnForm,RegForm,PasswordValidation

def showFormData(request):
    #fm=StudentRegistrationForm()
    #fm=StudentRegistrationForm(auto_id='some_%s')
    
    fm=StudentRegistrationForm(
        auto_id=True,label_suffix=" :- ",initial={'name':"kawsar",'email':'kawar@gmail.com'}
    )
    fm.order_fields(field_order=['email','name'])
    
    return render(request,"userRegistration.html",{'form':fm})

def MoreOnFormView(request):
    if request.method=="POST":
        fm=MoreOnForm(request.POST)
        if fm.is_valid():
            print(f"Name: {fm.cleaned_data['name']}")  
            print(f"DEPT: {fm.cleaned_data['dept']}")  
            print(f"SpaceValue: {fm.cleaned_data['withSpaceValue']}")  
            print(f"Agree: {fm.cleaned_data['agree']}")  
    else:
        fm=MoreOnForm()
    return render(request,"userRegistration.html",{'form':fm})

def formRegistration(request):
    if request.method=="POST":
        fm=RegForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data.get("name"))
    else:
        fm=RegForm()
    return render(request,"userRegistration.html",{'form':fm})

def passwordValidation(request):
    if request.method=="POST":
        fm=PasswordValidation(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data["name"])
    else:
        fm=PasswordValidation()
    return render(request,"userRegistration.html",{'form':fm})
