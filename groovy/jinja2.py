from bootstrap4.templatetags.bootstrap4 import bootstrap_form, bootstrap_messages, bootstrap_css, bootstrap_setting, \
    bootstrap_javascript
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'bootstrap_messages': bootstrap_messages,
        'bootstrap_form': bootstrap_form,
        'bootstrap_css': bootstrap_css,
        'bootstrap_setting': bootstrap_setting,
        'bootstrap_javascript': bootstrap_javascript
    })
    return env
