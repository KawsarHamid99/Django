from urllib import response
from django.shortcuts import render,HttpResponse

class siteUnderconstraction:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        response=render(request,"middleware/siteUC.html")
        print("------------------hello---------------")
        return response


