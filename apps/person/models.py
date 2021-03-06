from django.db import models
from django.core.urlresolvers import reverse
from apps.corporations.models import Corporation


class Person( models.Model ):
    name = models.CharField( max_length = 500, blank = True, null = True, db_index = True )
    personal_code = models.CharField( max_length = 200, db_index = True )
    address = models.TextField( blank = True, null = True )

    dob = models.DateField( blank = True, null = True )
    nationality = models.CharField( max_length = 200, blank = True, null = True )

    affiliations = models.ManyToManyField( Corporation, through = 'Affiliation', blank = True, null = True )

    '''
    the field will indicate whether the website should add a tag to the site presenting a person's information
    this will stop Google from inxexing this person's listing, thus not showing the details in search results.
    Also, this will remove private information from detail view
    '''
    no_index_tag = models.NullBooleanField( null = True, blank = True )

    def get_absolute_url( self ):
        return reverse( 'person-detail', args = [self.pk] )

    def affiliations_by_role_date( self ):
        return self.affiliation_set.all().order_by( 'role', '-valid_date' )

    def detail( self ):
        """ A very rough calculation of how much detail we have on this
        particular instance."""
        total = 0
        if self.name is not None:
            total += len( self.name )
        if self.address is not None:
            total += len( self.address )
        if self. nationality is not None:
            total += len( self.nationality )
            

class Affiliation( models.Model ):
    person = models.ForeignKey( Person )
    corp = models.ForeignKey( Corporation )
    role = models.CharField( max_length = 200, blank = True, null = True )

    cite_type = models.CharField( max_length = 100 )
    cite_link = models.URLField()

    # Date on which the affiliation is known to be valid
    valid_date = models.DateField( blank = True, null = True )

    share = models.FloatField( blank = True, null = True )

    class Meta:
        get_latest_by = 'valid_date'
     
