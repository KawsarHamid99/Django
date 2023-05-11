from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100,null=True,blank=True)