
import imp
from urllib import response

from django.http import HttpResponse


def my_middleware(get_response):
    print("One Time Initialization")
    def my_function(request):
        print("This is Before Views")
        response=get_response(request)
        print("This is my after view")
        return response
    return my_function

class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time brother Initialization")
    def __call__(self,request):
        print("this is brother before view")
        response=self.get_response(request)
        print("This is brother after view")
        return response

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time Father father Initialization")
    def __call__(self,request):
        print("this is father before view")
        #response=self.get_response(request)
        response=HttpResponse("chole jao sona")
        print("This is Father after view")
        return response

class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time mother Initialization")
    def __call__(self,request):
        print("this is Mother before view")
        response=self.get_response(request)
        print("This is Mother after view")
        return response