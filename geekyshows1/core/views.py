from django.shortcuts import render

def home(request):
    contaxt={'home':'active'}
    return render(request,"core/home.html",contaxt)


def contact(request):
    contaxt={'contact':'active'}
    return render(request,"core/contact.html",contaxt)
