from django import forms

class PersonSearchForm(forms.Form):
    name = forms.CharField(max_length=200,required=False)
    personal_code = forms.CharField(max_length=50,required=False,label="Personal number")
    address = forms.CharField(max_length=200,required=False)
