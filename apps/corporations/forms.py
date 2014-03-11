from django import forms
from django.forms import ModelForm, SplitDateTimeWidget
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from apps.corporations.fields import JqSplitDateTimeField
from apps.corporations.widgets import JqSplitDateTimeWidget
from django.utils.translation import ugettext_lazy as _

from .models import Corporation, Extract

class CorporationSearchForm(forms.Form):
    name = forms.CharField(max_length=250, required=False, label=_('Name'))
    id_code = forms.CharField(max_length=50, required=False, label=_('ID code'))
    address = forms.CharField(max_length=250, required=False, label=_('Address'))
    email = forms.CharField(max_length=250, required=False, label=_('Email'))
    companies_registered_after = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker','time_class':'timepicker', 'placeholder':'yyyy or yyyy-mm-dd'}), 
                                                      label=_('Companies registered after'))
    companies_registered_before = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker','time_class':'timepicker', 'placeholder':'yyyy or yyyy-mm-dd'}), 
                                                       label=_('Companies registered before'))

class CorporationForm(ModelForm):
    class Meta:
        model = Corporation

class ExtractForm(ModelForm):
    class Meta:
        model = Extract
