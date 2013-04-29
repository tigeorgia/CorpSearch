from apps.corporations.forms import CorporationSearchForm
from apps.person.forms import PersonSearchForm
from django.shortcuts import render_to_response

def home(request):
    corpsearch = CorporationSearchForm()
    personsearch = PersonSearchForm()
    return render_to_response('home.html', 
                                {'corpsearch': corpsearch,
                                 'personsearch': personsearch,})
