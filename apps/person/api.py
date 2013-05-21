from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.utils import trailing_slash
from .models import Person

class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        filtering = {
            "personal_code": ("exact"),
            "name": ALL,
            "address": ALL,
            "nationality": ALL,
        }
