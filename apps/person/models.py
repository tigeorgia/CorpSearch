from django.db import models
from apps.corporations.models import Corporation

#TODO: Consider adding db_index to name, personal_code
class Person(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    personal_code = models.CharField(max_length=50)
    address = models.CharField(max_length=200,blank=True,null=True)

    dob = models.DateField(null=True)
    nationality = models.CharField(max_length=100,blank=True,null=True)

    affiliations = models.ManyToManyField(Corporation, through='Affiliation')

    def detail(self):
        """ A very rough calculation of how much detail we have on this
        particular instance."""
        total = 0
        if self.name is not None:
            total+=len(self.name)
        if self.address is not None:
            total+=len(self.address)
        if self. nationality is not None:
            total+=len(self.nationality)

class Affiliation(models.Model):
    person = models.ForeignKey(Person)
    corp = models.ForeignKey(Corporation)
    role = models.CharField(max_length=200,blank=True,null=True)
    
    cite_type = models.CharField(max_length=100)
    cite_link = models.URLField()

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_ongoing = models.NullBooleanField() # Is the relationship ongoing?
