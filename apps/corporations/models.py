from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Corporation( models.Model ):
    # The legal ID code; this is what we usually mean when we
    # talk about a corporation's ID code
    id_code = models.CharField( max_length = 50, blank = True, null = True, db_index = True )
    # Corporations which are "individual entrepreneurs" may be known
    # by the personal ID code of the individual instead.
    personal_code = models.CharField( max_length = 100, blank = True, null = True )
    # No idea what this means, but some corporations have them.
    state_reg_code = models.CharField( max_length = 100, blank = True, null = True )
    # This is the primary key into the Public Registry's database.
    registry_db_code = models.CharField( max_length = 100 )

    name = models.CharField( max_length = 1000, db_index = True )

    registration_date = models.DateField( blank = True, null = True )

    def get_absolute_url( self ):
        return reverse( 'corporation-detail', args = [self.id_code] )

    def _get_registry_url( self ):
        return u"https://enreg.reestri.gov.ge/main.php?c=app&m=show_legal_person&legal_code_id={}".format( 
            self.registry_db_code )

    def get_latest_extract( self ):
        extracts = self.extract_set
        if extracts.count() > 0:
            return extracts.order_by( '-date' )[0]

    def affiliations_by_role_date( self ):
        return self.affiliation_set.all().order_by( 'role', '-valid_date' )

    latest_extract = property( get_latest_extract )
    registry_url = property( _get_registry_url )

    def __unicode__( self ):
        return self.name
    
    class Meta:
        managed = True


class LegalFormLookup( models.Model ):
    name = models.CharField( max_length = 250, blank = True, null = True )

    def __unicode__( self ):
        return self.name


class Extract( models.Model ):
    """ Certain types of info about corporations are stored only
    in documents called Extracts. In order to figure out the most up-to-date
    address and email address, we need to use Extracts."""
    date = models.DateTimeField( blank = True, null = True )
    address = models.TextField( blank = True, null = True )
    email = models.CharField( max_length = 750, blank = True, null = True )
    legalform = models.ForeignKey( LegalFormLookup, blank = True, null = True )
    corp = models.ForeignKey( 'Corporation' )
    corpurl = models.CharField( max_length = 750, blank = True, null = True )

    def __unicode__( self ):
        return self.corp
    
    class Meta:
        managed = True

