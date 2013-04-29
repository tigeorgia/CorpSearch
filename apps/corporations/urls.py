from django.conf.urls.defaults import patterns, url
from .views import CorporationListView, CorporationDetailView

urlpatterns = patterns('',
    url(r'^$', CorporationListView.as_view(), name='corporation-list'),
    url(r'^(?P<pk>\d+)/$', CorporationDetailView.as_view(), name='corporation-detail'),
)
