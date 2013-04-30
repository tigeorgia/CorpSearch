from django import forms

class CorporationSearchForm(forms.Form):
    name = forms.CharField(max_length=250, required=False)
    id_code = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=250, required=False)
    email = forms.CharField(max_length=250, required=False)
