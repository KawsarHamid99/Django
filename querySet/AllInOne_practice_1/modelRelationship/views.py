from django.shortcuts import render
from django.views import View
# Create your views here.
def home(request):
    return render(request,"modelRelationship/home.html")

class Home(View):
    def get(self,request):
        return render(request,'modelRelationship/home.html')
