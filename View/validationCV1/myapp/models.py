from gettext import translation
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Student(models.Model):
    name=models.CharField( _("Names"),max_length=100)
    roll=models.CharField( _('Rolls'),max_length=100)