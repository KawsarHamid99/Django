import email
from lib2to3.pgen2 import token
from msilib.schema import Class
from os import link
from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import EmailMessage 
from django.contrib.auth.models import User
from validate_email import validate_email
from django.urls import reverse

from .utils import token_generator


from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

import json
# Create your views here.
class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
         
    def post(self,request):
        #messages.success(request,"Success Whatsapp")
        #messages.error(request,"Success Whatsapp")
        username=request.POST["username"]
        email= request.POST["email"]
        password= request.POST["password"]
        context={
            'fieldValues':request.POST
        }


        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,'password is too short')
                    return render(request,'authentication/register.html',context)
                user=User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.is_active=False
                user.save()


                uidb64=str(urlsafe_base64_encode(user.pk))
                domain=get_current_site(request).domain
                link=reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})

                activate_url='http://'+domain+link
                email_subject='active your Acount'
                email_body="Hello "+user.username+ \
                    " Please use this link to verify your account\n "+activate_url
                
                email = EmailMessage(   
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],

                )
                email.send(fail_silently=False)
                messages.success(request,'account successfully created')
                return render(request,'authentication/register.html',context)



class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'usernameis invalid'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username is used,choose another one'},status=409)
        
        return JsonResponse({'username_valid':True})

class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        email=data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'email is not valid'},status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry this email is used,choose another one'},status=409)
        
        return JsonResponse({'email_valid':True})


class VerificationView(View):
    def get(self,request,uidb64,token):
        return redirect('login')


