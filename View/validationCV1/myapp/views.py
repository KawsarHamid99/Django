from django.shortcuts import render
from django.views import View
from .models import Student
from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.
class StudentDetail(DetailView):
    model=Student
    template_name='home.html'
    context_object_name='student'