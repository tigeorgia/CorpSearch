from django.conf.urls import *
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#TastyPie
from apps.corporations.api import CorporationResource
from apps.person.api import PersonResource
from tastypie.api import Api
v1_api = Api()
v1_api.register(CorporationResource())
v1_api.register(PersonResource())

urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
    (r'^$', views.home),
    (r'^corporations/', include('apps.corporations.urls')),
    (r'^people/', include('apps.person.urls')),

    # API via TastyPie
    url(r'^api/', include(v1_api.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
