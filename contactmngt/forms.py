from contactmngt.models import Team, Person
from django import forms
from django.core.exceptions import ObjectDoesNotExist


class TeamForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name'].lower()
        departement = cleaned_data['departement'].lower()
        partner = cleaned_data['partner']
        try:
            team = Team.objects.get(name__iexact=name, departement__iexact=departement, partner=partner)
            if self.instance != team:
                self.add_error('name', 'Name, department partner must be unique together')
        except ObjectDoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'street': forms.Textarea(attrs={'cols': '40', 'rows': '3'})
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'street': forms.Textarea(attrs={'cols': '40', 'rows': '3'})
        }