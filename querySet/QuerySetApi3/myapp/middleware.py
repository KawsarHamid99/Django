from urllib import response
from django.shortcuts import render,HttpResponse

class underconstraction:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("call form middleware")
        #response=self.get_response(request)
        #response=HttpResponse("site Under Constraction")
        response=render(request,"siteus.html")

        print("Call After View")
        return response