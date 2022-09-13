from django.shortcuts import render

from core.views import contact

# Create your views here.
def services(request):
    contaxt={'serv':'active'}
    return render(request,"service/services.html",contaxt)