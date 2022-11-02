from django.shortcuts import render

# Create your views here.
from .forms import StudentRegistrationForm, TeacherRegistrationForm

def showFormData(request):
    fm=StudentRegistrationForm(auto_id="sid_%s",label_suffix=" :- ",initial={'name':'Kawsar','email':'kawsar@gmail.com'})
    fm.order_fields(field_order=['email'])


    form2=TeacherRegistrationForm()
    return render(request,"renderFormMenually/renderform1.html",{'form':fm,'form2':form2 })