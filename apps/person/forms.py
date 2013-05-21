from django import forms
from .models import Person, Affiliation

class PersonSearchForm(forms.Form):
    name = forms.CharField(max_length=200,required=False)
    personal_code = forms.CharField(max_length=50,required=False,label="Personal number")
    address = forms.CharField(max_length=200,required=False)
    nationality = forms.CharField(max_length=200,required=False)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

class AffiliationForm(forms.ModelForm):
    class Meta:
        model = Affiliation
