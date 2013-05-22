from django.conf.urls.defaults import patterns, url
from .views import PersonPagedTemplateSearchView, PersonCsvSearchView, PersonDetailView

urlpatterns = patterns('',
    #Returns every person, of which there are over 160,000, so not recommended
    #to enable this.
    #url(r'^$', PersonListView.as_view(), name='person-list'),
    url(r'^(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person-detail'),
    url(r'^search/$', PersonPagedTemplateSearchView.as_view(template_name="person/person_list.html"), name='person-search'),
    url(r'^search/csv/$', PersonCsvSearchView.as_view(), name="person-search-csv"),
)
