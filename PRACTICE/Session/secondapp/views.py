from django.shortcuts import render,HttpResponse

# Create your views here.


def setsession(request):
    request.session['name']='kabila'
    request.session['id']=3222
    return render(request,'set.html')



def getsession(request):
    name=request.session.get('name','guest')
    request.session.set_expiry(110) 
    print("---------------------------------")
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request,"get.html",{"name":name})


def delsession(request):
    name=request.session.get("name",None)
    if name is not None:
        del request.session["name"]
    print(request.session.get("name","deleted")) 

    return HttpResponse("session deleted")

def flushsession(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponse("Session flush done.")


