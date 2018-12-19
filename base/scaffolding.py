# coding: utf-8
"""
CRUD
"""
from django.contrib.auth.decorators import login_required
from generic_scaffold import CrudManager

class BaseCrudManager(CrudManager):
    list_template_name = "base/list.html"
    detail_template_name = "base/detail.html"
    form_template_name = "base/form.html"
    update_template_name = "base/form.html"
    delete_template_name = "base/confirm_delete.html"

    permissions = {
        'update': login_required,
        'delete': login_required,
        'create': login_required,
    }
