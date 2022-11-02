from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def StudentView(request):
    fm=StudentForm()
    return render(request,"widgets/widget1.html",{'form':fm})