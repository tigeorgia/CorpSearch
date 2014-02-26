from django import forms
from .models import Person, Affiliation
from django.utils.translation import ugettext_lazy as _

class PersonSearchForm(forms.Form):
    name = forms.CharField(max_length=200,required=False,label=_('Name'))
    personal_code = forms.CharField(max_length=50,required=False,label=_("Personal number"))
    address = forms.CharField(max_length=200,required=False,label=_("Address"))
    nationality = forms.CharField(max_length=200,required=False,label=_("Nationality"))

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

class AffiliationForm(forms.ModelForm):
    class Meta:
        model = Affiliation
