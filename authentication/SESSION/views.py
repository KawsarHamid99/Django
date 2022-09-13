from email.policy import default
from django.shortcuts import render

# Create your views here.

def set_session(request):
    request.session["name"]="kawsar"
    #request.session["lname"]="Hamid"
    return render(request,"SESSION/set.html")


def get_session(request):
    
    if request.session:
        name=request.session.get('name')
        #request.session.set_expiry(0)
        #request.session.set_expiry(600)
    else:
        name="Tor nanir heda" 
    KEYS=request.session.keys()  
    ITEMS=request.session.items()


    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    print("")
    #set_default=request.session.setdefault("age","24")
    set_default=None
    return render(request,"SESSION/get.html",{"num":name,"keys":KEYS,"items":ITEMS,"set_default":set_default})

def delete_session(request):
    if "name" in request.session:
        del request.session["name"]
    return render(request,"SESSION/del.html")

def FLUSH_session(request):
    request.session.flush() #remove full session
    #request.session.clear_exp #clean the session form dataset
    return render(request,"SESSION/del.html")

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,"SESSION/set.html")
def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request,"SESSION/gettestcookie.html")
def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,"SESSION/del.html")


