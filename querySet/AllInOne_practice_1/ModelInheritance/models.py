from pyexpat import model
from weakref import proxy
from django.db import models

# Create your models here.

class commonInfo(models.Model):
    name=models.CharField(max_length=80)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True

class Student(commonInfo):
    dept=models.CharField(max_length=40)
    date=None


class Teacher(commonInfo):
    salary=models.FloatField()


class contractor(commonInfo):
    date=models.DateTimeField()


######one-to-one

class parent(models.Model):
    color=models.CharField(max_length=70)
    height=models.FloatField()
class child(parent):
    name=models.CharField(max_length=70)
    age=models.IntegerField()



##proxy class

class father(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    clr=models.CharField(max_length=80)

class son(father):
    class Meta:
        proxy=True
        ordering=['age']