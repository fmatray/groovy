from django import forms
from django_select2.forms import Select2TagWidget
from taggit.models import Tag


class BaseForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=Select2TagWidget, required=False)

    @classmethod
    def add_fields(cls, extra_fields):
        return ['name', 'status', 'tags', 'description', 'documentation'] + extra_fields + ['comment']

    class Meta:
        fields = '__all__'
