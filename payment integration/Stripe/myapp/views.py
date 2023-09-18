from django.shortcuts import render,HttpResponse
import stripe
from django.http import JsonResponse
from django.conf import settings
from .models import Product
stripe.api_key=settings.STRIPE_SECRET_KEY
# Create your views here.
def home(request):
    product=Product.objects.all()
    return render(request,"myapp/home.html",{'key':settings.STRIPE_PUBLIC_KEY,"product":product})

def charge(request,pk=None):
    product=None
    if pk:
        product=Product.objects.get(id=pk)
    if request.method == 'POST':
        charge=stripe.Charge.create(amount=int(product.price*100),currency='usd',description ='PAYMENT GATE WAY',source=request.POST['stripeToken'])
        return render(request,"myapp/charge.html")