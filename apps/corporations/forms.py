from django import forms
from django.forms import ModelForm

from .models import Corporation, Extract

class CorporationSearchForm(forms.Form):
    name = forms.CharField(max_length=250, required=False)
    id_code = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=250, required=False)
    email = forms.CharField(max_length=250, required=False)

class CorporationForm(ModelForm):
    class Meta:
        model = Corporation

class ExtractForm(ModelForm):
    class Meta:
        model = Extract
