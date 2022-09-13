from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class students(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=60)
    stupass=models.CharField(max_length=70)

    def __str__(self):
        return self.stuname
