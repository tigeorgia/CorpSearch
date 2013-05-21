from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.utils import trailing_slash
from .models import Corporation

class CorporationResource(ModelResource):
    class Meta:
        queryset = Corporation.objects.all()
        resource_name = 'corporation'
        filtering = {
            "id_code": ("exact"),
            "name": ALL,
            "address": ALL,
            "email": ALL,
        }
