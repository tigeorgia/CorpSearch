from django.conf.urls.defaults import patterns, url
from .views import CorporationListView

urlpatterns = patterns('',
    url(r'^$', CorporationListView.as_view(), name='corporation-list'),
)
