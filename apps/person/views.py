from .models import Person, Affiliation
from .forms import PersonSearchForm
from apps.util.views import CsvResponseMixin

from django.views.generic.list import BaseListView, ListView, MultipleObjectTemplateResponseMixin

from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class PersonListView(BaseListView):
    model = Person
    context_object_name = 'people'

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
            if form.cleaned_data['nationality']:
                qs = qs.filter(nationality__icontains=form.cleaned_data['nationality'])
        
        order_by_value = self.request.GET.get('order_by')
        if order_by_value:
            return qs.order_by(order_by_value)
        else:
            return qs.order_by('name')
        
        

class PersonPagedTemplateSearchView(PersonSearchView, MultipleObjectTemplateResponseMixin):
    paginate_by = 100

class PersonCsvSearchView(PersonSearchView, CsvResponseMixin):
    pass

class PersonDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'person/person_detail.html'
