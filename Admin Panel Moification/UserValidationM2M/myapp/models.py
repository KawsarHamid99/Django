from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user.username)+" "+str(self.age)

class MainContainer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    depertment=models.CharField(max_length=20)
    profilelist=models.ManyToManyField(UserProfile)

    def my_profilelist(self):
        return ",".join([str(p) for p in self.profilelist.all()])
    
    def __str__(self):
        return str(self.user.username)+" "+str(self.depertment)