from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Corporation, Extract

class CorporationSearchForm(forms.Form):
    name = forms.CharField(max_length=250, required=False, label=_('Name'))
    id_code = forms.CharField(max_length=50, required=False, label=_('ID code'))
    address = forms.CharField(max_length=250, required=False, label=_('Address'))
    email = forms.CharField(max_length=250, required=False, label=_('Email'))

class CorporationForm(ModelForm):
    class Meta:
        model = Corporation

class ExtractForm(ModelForm):
    class Meta:
        model = Extract
