from django.shortcuts import render
from .froms import Imageform
from .models import image

# Create your views here.
def home(request):
    if request.method=="POST":
        form=Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        form=Imageform()
    form=Imageform()
    img=image.objects.all()
    return render(request,"home.html",{"img":img,"form":form})

