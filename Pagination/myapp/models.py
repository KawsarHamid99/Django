from django.db import models

# Create your models here.
class Studentlist(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    faculty=models.CharField(max_length=200)