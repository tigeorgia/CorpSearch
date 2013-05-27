from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#TastyPie
from apps.corporations.api import CorporationResource
from apps.person.api import PersonResource
from tastypie.api import Api
v1_api = Api(api_name='v1')
v1_api.register(CorporationResource())
v1_api.register(PersonResource())

urlpatterns = i18n_patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
    (r'^$', views.home),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^corporations/', include('apps.corporations.urls')),
    (r'^people/', include('apps.person.urls')),

    # API via TastyPie
    url(r'^api/', include(v1_api.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
