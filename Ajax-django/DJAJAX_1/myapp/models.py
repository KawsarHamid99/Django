from django.db import models

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=100)
    national_id=models.CharField(max_length=10)
    city=models.CharField(max_length=100)

