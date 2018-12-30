from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms


class BaseModalForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    @classmethod
    def add_fields(cls, extra_fields):
        return ['name', 'status', 'tags', 'description'] + extra_fields + ['comment']

    class Meta:
        fields = '__all__'
