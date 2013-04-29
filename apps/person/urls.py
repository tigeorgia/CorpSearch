from django.conf.urls.defaults import patterns, url
from .views import PersonListView

urlpatterns = patterns('',
    url(r'^$', PersonListView.as_view(), name='person-list'),
)
