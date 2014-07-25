import codecs, os, sys

from django.core.management.base import BaseCommand, CommandError

import settings
from apps.corporations.load import corporations, extracts
from apps.corporations.models import Corporation, Extract
from apps.util.models import ScraperStat
from apps.person.load import people
from apps.person.models import Person, Affiliation
from datetime import datetime

class Command(BaseCommand):
    help = "Reloads corporation data from the 'data' directory."

    CORP_DATA = "Corporation.json"
    EXTRACT_DATA = "RegistryExtract.json"
    DATA_FOLDER = 'data'

    def handle(self, *args, **options):
        
        #importCorpsStartDate = datetime.datetime.now()
        
        """ Loads corporations data from data files."""
        if settings.DEBUG == True:
            raise Exception("Please set settings.DEBUG to False unless you like OutOfMemory errors.")
        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.CORP_DATA), encoding="utf-8-sig") as corp_file:
            print("Loading corporation data")
            corporations.load_corporations(corp_file)

        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.EXTRACT_DATA), encoding="utf-8-sig") as extract_file:
            print("Loading extract data")
            extracts.load_extracts(extract_file)
            
        #importCorpsFinishDate = datetime.datetime.now()
            
        #obj = ScraperStat(import_corps_start=importCorpsStartDate, import_corps_finish=importCorpsFinishDate)
        #obj.save()

