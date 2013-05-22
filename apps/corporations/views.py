from .models import Corporation
from .forms import CorporationSearchForm
from apps.util.views import CsvResponseMixin

from django.views.generic.list import ListView, BaseListView, MultipleObjectTemplateResponseMixin
from django.views.generic.detail import DetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class CorporationListView(BaseListView):
    model = Corporation
    context_object_name = 'corporations'

class CorporationSearchView(CorporationListView):
    def get_queryset(self):
        qs = super(CorporationSearchView, self).get_queryset()

        form = CorporationSearchForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['id_code']:
                qs = qs.filter(id_code=form.cleaned_data['id_code'])
            if form.cleaned_data['address']:
                qs = qs.filter(extract__address__icontains=form.cleaned_data['address']).distinct()
            if form.cleaned_data['email']:
                qs = qs.filter(extract__email__icontains=form.cleaned_data['email']).distinct()
            if form.cleaned_data['name']:
                qs = qs.filter(name__icontains=form.cleaned_data['name'])

        return qs.order_by('name')

class CorporationPagedTemplateSearchView(CorporationSearchView, MultipleObjectTemplateResponseMixin):
    paginate_by = 25

class CorporationCsvSearchView(CorporationSearchView, CsvResponseMixin):
    pass

class CorporationDetailView(DetailView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'corporations/detail.html'
