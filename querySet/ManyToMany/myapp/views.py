from django.shortcuts import render,HttpResponse
from .models import Song

# Create your views here.
def home(request):
    song=Song.objects.all()
    print(f'---------------------------------------------------')
    print(song[2].written_by())
    print(song[2].user.all().first().email)
    return HttpResponse("hello world")