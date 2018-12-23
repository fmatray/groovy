from django import template

register = template.Library()

@register.simple_tag
def create_list(*args, **kwargs):
    return [*args]

@register.simple_tag
def create_dict(*args, **kwargs):
    return kwargs