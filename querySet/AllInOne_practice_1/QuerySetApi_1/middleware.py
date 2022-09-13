from urllib import response
from django.shortcuts import render,HttpResponse

class siteunderconstraction:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("Before middleware")
        response=self.get_response(request)
        response=HttpResponse("hello from middleware")
        response=render(request,"middleware/siteUC.html")
        print('After response')
        return response
