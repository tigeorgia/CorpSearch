from .models import Person, Affiliation

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'person/person_list.html'

class PersonSearchView(PersonListView):
    def get_queryset(self):
        qs = Person.objects.all()
        if self.request.GET.get('p_code'):
            qs = qs.filter(personal_code=self.request.GET.get('p_code'))
        if self.request.GET.get('name'):
            qs = qs.filter(name__icontains=self.request.GET.get('name'))
        if self.request.GET.get('address'):
            qs = qs.filter(address__icontains=self.request.GET.get('address'))
        return qs


class PersonDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'person/person_detail.html'
