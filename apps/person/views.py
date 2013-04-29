from .models import Person

from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'person/person_list.html'
