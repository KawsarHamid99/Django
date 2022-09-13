
from django.shortcuts import HttpResponse
from django.template.response import TemplateResponse

class mummymiddlewire:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time Initialization")
    def __call__(self,request):
        print("This is mummy before view")
        response=self.get_response(request)
        print("mummy after view")
        return response


class MyprocessMidleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_view(request,*args,**kwargs):
        print("process view - Before view")
        #return HttpResponse("This is before view")
        return None


class myExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        print("exception occured")
        msg=exception
        class_name=exception.__class__.__name__
        print(msg)
        print(class_name)
        return HttpResponse(msg)


class templateExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_template_response(self,request,response):
        print("process Template Response From Middleware")
        response.context_data["name"]="kabila"
        return response

