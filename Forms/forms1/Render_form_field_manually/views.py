from django.shortcuts import render
from .froms import StudentForm
def home(request):
    
    #form=StudentForm(label_suffix=" : ",auto_id=True,field_order=["name","first_name"],initial={"name":'kanila'})
    form=StudentForm()
    if request.method=="POST":
        print(request.POST["name"])
        #print(request.POST["email"])
    return render(request,"render_FM/base.html",{'form':form})

        