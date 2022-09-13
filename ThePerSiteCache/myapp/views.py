
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from django.core.cache import cache

# Create your views here.

#@cache_page(20)
def home(request):
    mv=cache.get('movie',"has_expired")
    if mv == 'has_expired':
        cache.set("movie","the manjhi",30)
        mv=cache.get('movie')
    return render(request,"home.html",{"fm":mv})

def home2(request):
    #mv=cache.get_or_set('fees',4000,20)
    mv=cache.get_or_set('fees',4000,20,version=2)

    data={"name":"kawsar","roll":220}
    cache.set_many(data,30)
    sv=cache.get_many(data)
    return render(request,"home.html",{"fm":mv,"stu":sv})

#@cache_page(0)
def contact(request):
    return render(request,"contact.html")


def base(request):
    return render(request,"base.html")


def delete(request):
    #cache.delete("fees")
    #cache.delete("fees",version=2)
    cache.set("roll",100,20)
    #cache.decr("roll",delta=3)
    fm=cache.get("roll")
    print(fm)
    return render(request,"home.html",{"fm":fm})

def clr_cache(request):
    cache.clear()
    fm=cache.get("roll")
    return render(request,"home.html",{"fm":fm})
    

