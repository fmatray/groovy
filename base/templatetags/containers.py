from django import template

register = template.Library()


@register.simple_tag
def create_list(*args, **kwargs):
    return [*args]


@register.simple_tag
def create_sorted_list(*args, **kwargs):
    return sorted([*args])


@register.simple_tag
def create_dict(*args, **kwargs):
    return kwargs


@register.simple_tag
def create_set(*args, **kwargs):
    return {*args}


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(',')
