from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def home(request):

    dest1=Destination()
    dest1.name="CHANDPUR"
    dest1.img="destination_1.jpg"
    dest1.price=1000
    dest1.desc="citis of Hilsha"
    dest1.offer=True
    
    dest2=Destination()
    dest2.img="destination_3.jpg"
    dest2.name="COMILLA"
    dest2.price=600
    dest2.desc="The City where people pies "
    dest2.offer=False

    dest3=Destination()
    dest3.img="destination_2.jpg"
    dest3.name="DHAKA"
    dest3.price=300
    dest3.desc="city of masque"
    dest3.offer=True

    dest4=Destination()
    dest4.name="CHITTAGONG"
    dest4.img="destination_9.jpg"
    dest4.price=800
    dest4.desc="port city of bangladesh"
    dest4.offer=False

    #dest=[dest1,dest2,dest3,dest4]
    dest=Destination.objects.all()
    
    return render(request,"index.html",{"dests":dest})