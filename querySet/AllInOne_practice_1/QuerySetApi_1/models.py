from unicodedata import name
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=40)
    roll=models.IntegerField(unique=True,null=False)
    dept=models.CharField(max_length=70)
    marks=models.FloatField()
    pass_date=models.DateField()

class Teacher(models.Model):
    name=models.CharField(max_length=70)
    empnum=models.IntegerField()
    dept=models.CharField(max_length=70)
    salary=models.IntegerField()
    join_date=models.DateField()
