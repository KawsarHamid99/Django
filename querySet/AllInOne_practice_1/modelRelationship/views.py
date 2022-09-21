from django.shortcuts import render
from django.views import View
# Create your views here.
def home(request):
    return render(request,"modelRelationship/home.html")

class Home(View):
    def get(self,request):
        return render(request,'modelRelationship/home.html')

def page(request):
    return render(request,"modelRelationship/page.html")

def post(request):
    return render(request,"modelRelationship/post.html")

def song(request):
    return render(request,"modelRelationship/song.html")

def user(request):
    return render(request,"modelRelationship/user.html")