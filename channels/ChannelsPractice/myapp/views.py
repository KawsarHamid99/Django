from django.shortcuts import render,HttpResponseRedirect,HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")