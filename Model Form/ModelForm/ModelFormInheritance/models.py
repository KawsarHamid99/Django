from django.db import models

# Create your models here.
class Registration(models.Model):
    student_name=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()

    depertment=models.CharField(max_length=20)