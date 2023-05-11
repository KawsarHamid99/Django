from django import template
from ..models import Student

register=template.Library()

@register.simple_tag
def total_stu():
    return Student.objects.all()