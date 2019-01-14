from django import forms


class BaseForm(forms.ModelForm):
    chg_reason = forms.CharField(label="Change reason", required=False)

    @classmethod
    def add_fields(cls, extra_fields):
        return ['name', 'status', 'tags', 'description', 'documentation'] + extra_fields + ['comment']

    def save(self, commit=True):
        self.instance.changeReason = self.cleaned_data['chg_reason']
        return super().save(commit)

    class Meta:
        fields = '__all__'
