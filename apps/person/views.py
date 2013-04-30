from .models import Person, Affiliation
from .forms import PersonSearchForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class PersonListView(ListView):
    paginate_by = 25
    model = Person
    context_object_name = 'people'
    template_name = 'person/person_list.html'

class PersonSearchView(PersonListView):
    def get_queryset(self):
        qs = super(PersonSearchView, self).get_queryset()

        form = PersonSearchForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['personal_code']:
                qs = qs.filter(personal_code=form.cleaned_data['personal_code'])
            if form.cleaned_data['name']:
                qs = qs.filter(name__icontains=form.cleaned_data['name'])
            if form.cleaned_data['address']:
                qs = qs.filter(address__icontains=form.cleaned_data['address'])
        return qs


class PersonDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'person/person_detail.html'
