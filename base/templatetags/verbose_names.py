from django import template

register = template.Library()

@register.filter
def object_verbose_name(object):
    return object._meta.verbose_name

@register.filter
def object_verbose_name_plural(object):
    return object._meta.verbose_name_plural

@register.filter
def object_field_verbose_name(object, field):
    try:
        return object._meta.get_field(field).verbose_name
    except:
        return object._meta.get_field(field).field.model._meta.verbose_name_plural