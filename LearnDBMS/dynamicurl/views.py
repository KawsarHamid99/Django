from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"dynamicurl/home.html")

''' 
def dynamic(request,my_id):
    return render(request,"dynamicurl/dynamic.html",{"id":my_id})
'''
def dynamic(request,my_id):
    if my_id==1:
        info={"id":my_id,"name":"kawsar"}
        
    if my_id==2:
        info={"id":my_id,"name":"Rakib"}
    
    if my_id==3:
        info={"id":my_id,"name":"Baki"}
    if my_id==4:
        info={"id":my_id,"name":"Faki"}

    return render(request,"dynamicurl/dynamic.html",info)