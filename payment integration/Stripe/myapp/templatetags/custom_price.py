from django import template
register=template.Library()

@register.simple_tag
def price(value):
    return value*100