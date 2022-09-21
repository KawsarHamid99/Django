from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')

class extra_customManager(models.Manager):
    def get_roll_range(self,r1,r2):
        return super().get_queryset().filter(roll__range=(r1,r2))

class doublte_extra_customManager(models.Manager):
    def roll_range(self,r1,r2):
        return super().get_queryset().filter(age__range=(r1,r2))