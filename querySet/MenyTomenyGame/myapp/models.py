from django.db import models

# Create your models here.

class RAM(models.Model):
    name=models.CharField(max_length=100,unique=True)
    size=models.CharField(max_length=100)
    def __str__(self):
        return str(self.name+" "+self.size)
    
class SSD(models.Model):
    name=models.CharField(max_length=100,unique=True)
    size=models.CharField(max_length=100)
    recommendade_RAM=models.ManyToManyField(RAM,blank=True)

    def ram_list(self):
        return ",".join(str(p.name) for p in self.recommendade_RAM.all())
    def __str__(self):
        return str(self.name+" "+self.size)
    
class Processor(models.Model):
    name=models.CharField(max_length=100,unique=True)
    size=models.CharField(max_length=100)
    recommendade_RAM=models.ManyToManyField(RAM,blank=True)
    recommendade_SSD=models.ManyToManyField(SSD,blank=True)
    def ram_list(self):
        return ",".join(str(p.name) for p in self.recommendade_RAM.all()) 
    
    def ssd_list(self):
        return ",".join(str(p.name) for p in self.recommendade_SSD.all())
    
    def __str__(self):
        return str(self.name+" "+self.size)
    

class Product(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    processor=models.ManyToManyField(Processor,blank=True)

    def processor_list(self):
       return ",".join(str(p.name) for p in self.processor.all())

    def __str__(self):
        return str(self.name)
