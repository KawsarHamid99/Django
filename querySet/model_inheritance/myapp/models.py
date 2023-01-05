from re import L
from unicodedata import name
from weakref import proxy
from django.db import models

class CommonInfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    
    class Meta:
        abstract=True 

class St(CommonInfo):
    fees=models.IntegerField()
    #date=None

class Teacher(CommonInfo):
    salary=models.IntegerField()


class Contractor(CommonInfo):
    date=models.DateTimeField()    


############# One To One 
# If you remove a data from parents class,child class's data also be deleted if data is not present in child class only parent class data will be deleted
# If you remove a data from child class,parents class's data also be deleted

class parents(models.Model):
    clr=models.CharField(max_length=30)
    height=models.FloatField()
class Child(parents):
    name=models.CharField(max_length=60)
    age=models.IntegerField()   



####Proxy Model
# it won't change the data,just change the behavior of the model
class father(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    clr=models.CharField(max_length=40)


class son(father):
    class Meta:
        proxy=True
        ordering=['age'] 

        
