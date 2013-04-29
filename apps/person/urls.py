from django.conf.urls.defaults import patterns, url
from .views import PersonListView, PersonSearchView, PersonDetailView

urlpatterns = patterns('',
    url(r'^$', PersonListView.as_view(), name='person-list'),
    url(r'^(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person-detail'),
    url(r'^search/$', PersonSearchView.as_view(), name='person-search')
)
