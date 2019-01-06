from django import template

register = template.Library()

# Custom tag for diagnostics
@register.simple_tag
def debug_object_dump(var):
    try:
        return "{}:{}:{}".format(var, var.__class__.__name__ , vars(var))
    except:
        return "{}:{}".format(var, var.__class__.__name__ )