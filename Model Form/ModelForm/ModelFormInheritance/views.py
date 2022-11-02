from django.shortcuts import render
from .forms import StudentRegistrationForm,TeacherRegistrationForm
from .models import Registration
# ModelFormInheritance


def StudentView(request):
    if request.method=="POST":
        fm=StudentRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=StudentRegistrationForm()
    return render(request,"ModelFormInheritance/ValueForm.html",{'form':fm})



def TeacherView(request):
    if request.method=="POST":
        fm=TeacherRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=TeacherRegistrationForm()
    return render(request,"ModelFormInheritance/ValueForm.html",{'form':fm})


