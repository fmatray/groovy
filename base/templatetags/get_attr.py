from django import template

register = template.Library()

@register.filter
def get_obj_attr(obj, attr):
    try:
        return getattr(obj, attr)
    except AttributeError:
        return None

@register.filter
def get_obj_attr_list(obj, attr):
    try:
        return getattr(obj, attr).all()
    except AttributeError:
        return None
