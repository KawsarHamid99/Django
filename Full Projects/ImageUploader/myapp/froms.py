from cProfile import label
from dataclasses import field
from pyexpat import model
from tkinter import Image
from django import forms
from .models import image

class Imageform(forms.ModelForm):
    class Meta:
        model=image
        fields='__all__'
        labels={'photo':""}

