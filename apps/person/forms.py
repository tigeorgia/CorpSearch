from django import forms
from .models import Person, Affiliation
from django.utils.translation import ugettext_lazy as _

class PersonSearchForm(forms.Form):
    name = forms.CharField(max_length=200,required=False,label=_('Full Name'),
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    personal_code = forms.CharField(max_length=50,required=False,label=_("Personal number"),
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=1500,required=False,label=_("Address"),
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    nationality = forms.CharField(max_length=200,required=False,label=_("Nationality"),
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ['name', 'personal_code', 'address', 'dob', 'nationality', 'affiliations']
# 
# class AffiliationForm(forms.ModelForm):
#     class Meta:
#         model = Affiliation
#         fields = ['person', 'corp', 'role', 'cite_type', 'cite_link', 'valid_date', 'share']