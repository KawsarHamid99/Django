from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session['name']='kabila'
    request.session['id']=1221
    return render(request,"setsession.html")


def getsession(request):
    name=request.session.get("name","guest")
    print("---------------------------------------")
    request.session.set_expiry(5)
    #request.session.set_expiry(0)
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request,"getsession.html",{'name':name})

def delsession(request):
    name=request.session['name']
    if name == "kawsar":
        del request.session['name']
    else:
        return HttpResponse("Name is not found")
    return render(request,"delsession.html")


def flushsession(request):
    request.session.flush()
    #request.session.clear_expired()
    return render(request,"delsession.html")


def set_test_session(request):
    request.session.set_test_cookie()
    return render(request,"set_test_cookie.html")

def check_test_session(request):
    print(request.session.test_cookie_worked())
    return render(request,"check_test_cookie.html")

def del_test_session(request):
    request.session.delete_test_cookie()
    return render(request,"del_test_cookie.html")