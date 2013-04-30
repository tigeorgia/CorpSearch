from .models import Corporation
from .forms import CorporationSearchForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class CorporationListView(ListView):
    model = Corporation
    context_object_name = 'corporations'
    template_name = 'corporations/corporation_list.html'

class CorporationSearchView(CorporationListView):
    def get_queryset(self):
        qs = super(CorporationSearchView, self).get_queryset()

        form = CorporationSearchForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['id_code']:
                qs = qs.filter(id_code=form.cleaned_data['id_code'])
            qs = qs.filter(name__icontains=form.cleaned_data['name'])

        return qs

class CorporationDetailView(DetailView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'corporations/detail.html'
