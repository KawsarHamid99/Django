from django.shortcuts import render

from .models import Destination

# Create your views here.

def index(request):
    '''
        dest1=Destination()
    dest1.name="DHAKA"
    dest1.price=800
    dest1.desc="city of mosque"
    dest1.img="destination_1.jpg"
    dest1.offer=True

    dest2=Destination()
    dest2.name="KHULNA"
    dest2.price=700
    dest2.desc="Place of Royal Bangle Tiger"
    dest2.offer=True
    dest2.img="destination_2.jpg"

    dest3=Destination()
    dest3.name="CHITTAGONG"
    dest3.price=900
    dest3.desc="city of mosque"
    dest3.offer=False
    dest3.img="destination_3.jpg"
    dest=[dest1,dest2,dest3]
    '''
    dest= Destination.objects.all()
    return render(request,"index.html",{"dest": dest })
