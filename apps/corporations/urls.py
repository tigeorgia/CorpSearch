from django.conf.urls.defaults import patterns, url
from .views import CorporationListView, CorporationSearchView, CorporationDetailView

urlpatterns = patterns('',
    url(r'^$', CorporationListView.as_view(), name='corporation-list'),
    url(r'^(?P<pk>\d+)/$', CorporationDetailView.as_view(), name='corporation-detail'),
    url(r'^search/$', CorporationSearchView.as_view(), name='corporation-search'),
)
