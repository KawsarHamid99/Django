
from django.db import models

# Create your models here.
class StudentModels(models.Model):
    name=models.CharField(max_length=100, blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField( max_length=100,blank=True,null=True)