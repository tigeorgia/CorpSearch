from apps.corporations.forms import CorporationSearchForm
from apps.corporations.models import Corporation, LegalFormLookup
from apps.person.models import Person
from apps.util.models import ScraperStat
from apps.person.forms import PersonSearchForm
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    corpsearch = CorporationSearchForm()
    personsearch = PersonSearchForm()
    last_scraping_update = ScraperStat.objects.all().order_by('-import_people_finish')[0]

    corpCount = Corporation.objects.all().count()
    personCount = Person.objects.all().count()

    return render_to_response('home.html',
                              {'corpsearch': corpsearch,
                               'personsearch': personsearch,
                               'lastUpdateDate': last_scraping_update,
                               'corpCount': corpCount,
                               'personCount': personCount},
                              context_instance=RequestContext(request), )


def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))

