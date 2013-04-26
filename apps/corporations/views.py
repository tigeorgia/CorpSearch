from .models import Corporation

from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class CorporationListView(ListView):
    model = Corporation
    context_object_name = 'corporations'
    template_name = 'corporations/corporation_list.html'
