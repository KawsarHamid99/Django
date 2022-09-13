import email
import imp
from django.shortcuts import render
from .models import Page,Post,User,Song
# Create your views here.

def home(request):
    return render(request,'home.html')


def show_user_data(request):
    data1=User.objects.all()
    data2=User.objects.filter(email="kawsar@gmail.com")
    data3=User.objects.filter(page__page_cat='Programming')
    data4=User.objects.filter(post__post_published_date='2020-05-22')
    data5=User.objects.filter(song__song_duration=5)
    return render(request,'user.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,})



def show_user_page(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(page_cat='Programming')
    data3=Page.objects.filter(user__email='Israt@gmail.com')  
    
    
    return render(request,'page.html',{'data1':data1,'data2':data2,'data3':data3,})


def show_post_data(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(post_published_date='2020-05-22')
    data3=Post.objects.filter(user__username='motin')  
    
    
    return render(request,'post.html',{'data1':data1,'data2':data2,'data3':data3,})

    
def show_song_data(request):
    data1=Song.objects.all()
    data2=Song.objects.filter(song_duration=5)
    data3=Song.objects.filter(user__username='motin')  
    
    
    return render(request,'song.html',{'data1':data1,'data2':data2,'data3':data3,})

