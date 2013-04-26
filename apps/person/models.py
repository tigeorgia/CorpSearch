from django.db import models
from apps.corporations.models import Corporation

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    personal_code = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=200,blank=True,null=True)

    dob = models.DateField()
    nationality = models.CharField(max_length=100,blank=True,null=True)

    affiliations = models.ManyToManyField(Corporation, through='Affiliation')

class Affiliation(models.Model):
    person = models.ForeignKey(Person)
    corp = models.ForeignKey(Corporation)
    role = models.CharField(max_length=200,blank=True,null=True)
    
    cite_type = models.CharField(max_length=100)
    cite_link = models.URLField()

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_ongoing = models.NullBooleanField() # Is the relationship ongoing?
