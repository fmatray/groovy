from django import forms


class BaseForm(forms.ModelForm):

    @classmethod
    def add_fields(cls, extra_fields):
        return ['name', 'status', 'tags', 'description'] + extra_fields + ['comment']

    class Meta:
        fields = '__all__'
