from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def home(request):
    if request.method == "POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=StudentForm()
    return render(request,"base.html",{'form':fm})