import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contract(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    desc=models.TextField()