from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #when you remove User data,Pages data will be deleted automatically,but if you delete Pages data thn only page data will be removed

    
    #user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    #here you can't delete User data until you remove pages data

    #user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={"is_staff":True})
    #if staff status is not activate thn can not create pages







    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_published_date=models.DateField()
