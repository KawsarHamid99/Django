from django.shortcuts import render

from modelManager.manager import doublte_extra_customManager
from .models import Mother,daughter
# Create your views here.
def home(request):
    data=Mother.objCM.all()
    
    data2=daughter.objects.all()
    data2=daughter.objDECM.roll_range(10,30)
    data2=daughter.objects.filter(age__range=(10,35))
    return render(request,"modelManager/base.html",{'data':data,'data2':data2})