from urllib import response
from django.shortcuts import HttpResponse,render
class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("Call From Middleware")
        #response=self.get_response(request)
        #response=HttpResponse("This is under Constraction")
        response=render(request,'siteuc.html')
        print("call after view")
        return response