from django import forms
from django.forms import ModelForm, SplitDateTimeWidget
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from apps.corporations.fields import JqSplitDateTimeField
from apps.corporations.widgets import JqSplitDateTimeWidget
from django.utils.translation import ugettext_lazy as _
from apps.corporations.models import LegalFormLookup

from .models import Corporation, Extract


class CorporationSearchForm(forms.Form):
    name = forms.CharField(max_length=250, required=False, label=_('Company Name'),
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_code = forms.CharField(max_length=50, required=False, label=_('ID code'),
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=1500, required=False, label=_('Address'),
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=250, required=False, label=_('Email'),
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    legal_form = forms.ModelChoiceField(queryset=LegalFormLookup.objects.all(), required=False, label=_('Legal Form'),
                                        widget=forms.Select(attrs={'class': 'form-control'}))

    companies_registered_after = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker form-control','time_class':'timepicker', 'placeholder':'yyyy or yyyy-mm-dd'}),
                                                      label=_('Companies registered after'))
    companies_registered_before = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker form-control','time_class':'timepicker', 'placeholder':'yyyy or yyyy-mm-dd'}),
                                                       label=_('Companies registered before'))
    
    

# class CorporationForm(ModelForm):
#     class Meta:
#         model = Corporation
#         fields = ['id_code', 'personal_code', 'name', 'registration_date']
# 
# 
# class ExtractForm(ModelForm):
#     class Meta:
#         model = Extract
#         fields = ['date', 'address', 'email', 'legalform', 'corp', 'corpurl']
