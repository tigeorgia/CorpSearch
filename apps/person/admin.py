'''
Created on Dec 10, 2014

@author: msuliga
'''
from django.contrib import admin
from .models import Person

class PersonAdmin( admin.ModelAdmin ):
    search_fields = ['name']
    list_display = ( 'name', 'address', 'no_index_tag', 'id' )
    list_editable = ('no_index_tag',)
    fields = [ 'no_index_tag']    
        
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    
admin.site.register( Person, PersonAdmin )
