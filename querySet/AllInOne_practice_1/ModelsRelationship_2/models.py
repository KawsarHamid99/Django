from django.db import models



class student(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=70)
    marks=models.IntegerField()
    pass_date=models.DateField()
    admitdate=models.DateTimeField()
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name=models.CharField(max_length=70)
    empnum=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=70)
    salary=models.IntegerField()
    join_date=models.DateField()

    def __str__(self):
        return self.name