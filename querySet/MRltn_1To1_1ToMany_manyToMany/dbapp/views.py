from django.shortcuts import render,HttpResponse
from django.views.generic import View
from .models import Person,City,Interest,Personaddress
# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        allperson=Person.objects.all()
        print("----------------------------------------------------------------------------------------------")
        print(allperson)
        for i in allperson:
            print(i.name)
            print(i.interest.all())
            for j in i.interest.all():
                print(j)
        print("----------------------------------------------------------------------------------------------")
        #print(Person.objects.get(id=1).interest.all())
        person=Person.objects.get(id=1)
        address=person.personaddress
        #print(address)
        print(address.city)
        print(address.street_address)
        print(address.person)
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")
        city=City.objects.get(id=5).personaddress_set.all()
        print(city)
        for j in city:
            print(j.person)

        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")
        
        interest=Interest.objects.get(id=2)
        print(interest)
        interested_person=interest.person_set.all()
        print(interested_person)
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")
        Paddress=Personaddress.objects.all()
        print(Paddress[0].city)
        context={}
        return render(request,'home.html',context)
        

def home(request):
    return HttpResponse("Hello from home.")