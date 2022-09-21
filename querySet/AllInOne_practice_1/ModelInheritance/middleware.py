from django.shortcuts import HttpResponse,render

class getMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("before middleware")
        return render(request,'middleware/siteUC.html')
