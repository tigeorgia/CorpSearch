from .models import Person, Affiliation

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'person/person_list.html'

class PersonDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'person/person_detail.html'
