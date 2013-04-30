from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Corporation(models.Model):
    # The legal ID code; this is what we usually mean when we 
    # talk about a corporation's ID code
    id_code = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    # Corporations which are "individual entrepreneurs" may be known
    # by the personal ID code of the individual instead.
    personal_code = models.CharField(max_length=50,blank=True,null=True)
    # No idea what this means, but some corporations have them.
    state_reg_code = models.CharField(max_length=50,blank=True,null=True)
    # This is the primary key into the Public Registry's database.
    registry_db_code = models.CharField(max_length=50)
    
    name = models.CharField(max_length=250)

    registration_date = models.DateField()

    def get_absolute_url(self):
        return reverse('corporation-detail', args=[self.pk])

    def _get_registry_url(self):
        return u"https://enreg.reestri.gov.ge/main.php?c=app&m=show_legal_person&legal_code_id={}".format(self.registry_db_code)
    registry_url = property(_get_registry_url)

class Extract(models.Model):
    """ Certain types of info about corporations are stored only
    in documents called Extracts. In order to figure out the most up-to-date
    address and email address, we need to use Extracts."""
    date = models.DateField(null=True)
    address = models.CharField(max_length=250,null=True)
    email = models.CharField(max_length=250,null=True)
    corp = models.ForeignKey('Corporation')

