from distutils.command import upload
from django.db import models

# Create your models here.
class Destination(models.Model):
    price=models.IntegerField()
    name=models.CharField(max_length=200)
    desc=models.TextField()
    offer=models.BooleanField(default=False)
    img=models.ImageField(upload_to='pics')