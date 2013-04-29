from .models import Corporation

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
        qs = Corporation.objects.all()
        if self.request.GET.get('id_code'):
            qs = qs.filter(id_code=self.request.GET.get('id_code'))
        if self.request.GET.get('name'):
            qs = qs.filter(name__icontains=self.request.GET.get('name'))
        return qs

class CorporationDetailView(DetailView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'corporations/detail.html'
