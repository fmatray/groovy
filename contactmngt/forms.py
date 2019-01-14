from appmngt.models.partner import Partner
from contactmngt.models import Team, Person
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django_select2.forms import ModelSelect2Widget


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'partner': ModelSelect2Widget(queryset=Partner.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'street': forms.Textarea(attrs={'cols': '40', 'rows': '3'})
        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'street': forms.Textarea(attrs={'cols': '40', 'rows': '3'})
        }
