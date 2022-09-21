from weakref import proxy
from django.db import models
from .manager import CustomManager,doublte_extra_customManager
# Create your models here.
class Mother(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()

    objCM=CustomManager()
    objects=models.Manager()
    objDECM=doublte_extra_customManager()


class daughter(Mother):
    class Meta:
        proxy=True
        ordering=["age"]
