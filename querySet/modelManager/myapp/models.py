from django.db import models
from .managers import CustomManager,Extra_CustomManager

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()

    objects=models.Manager()
    students=CustomManager()

    #add extra manager
    stu=Extra_CustomManager()


class Proxystudent(Student):
    proxymanager=Extra_CustomManager()
    class Meta:
        proxy=True
        ordering=["name"]
