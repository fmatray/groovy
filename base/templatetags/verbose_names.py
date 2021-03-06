from django import template

register = template.Library()


@register.filter
def object_verbose_name(object):
    return object._meta.verbose_name


@register.filter
def object_verbose_name_plural(object):
    try:
        return object._meta.verbose_name_plural
    except AttributeError:
        return None


@register.filter
def get_table_verbose_name_plural(obj):
    try:
        return obj._meta.model._meta.verbose_name_plural
    except AttributeError:
        return None


@register.filter
def object_field_verbose_name(object, field):
    if hasattr(object, field) and callable(getattr(object, field)) and hasattr(getattr(object, field), "verbose_name"):
        return getattr(object, field).verbose_name
    else:
        try:
            return object._meta.get_field(field).verbose_name
        except AttributeError:
            try:
                return "{} {}".format(object._meta.get_field(field).field.verbose_name,
                                      object._meta.get_field(field).field.model._meta.verbose_name_plural)
            except:
                return None
