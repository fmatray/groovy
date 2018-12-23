from crispy_forms.helper import FormHelper


def get_helper():
    helper = FormHelper()
    helper.form_class = 'form'
    helper.field_classes = 'form-control-sm'
    helper.template_pack = 'bootstrap4'
    return helper


def get_inline_helper():
    helper = get_helper()
    helper.form_class = 'form form-inline'
    helper.label_class = 'col'
    helper.field_class = 'col'
    helper.form_class = 'form form-inline'
    return helper