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
    help = "Reloads data from the 'data' directory."

    AFFILIATION_DATA = "PersonCorpRelation.json"
    DATE_DATA = "StatementDocument.json"
    DATA_FOLDER = 'data'

    def handle(self, *args, **options):
        """ Loads new person data."""
        if settings.DEBUG == True:
            raise Exception("Please set settings.DEBUG to False unless you like OutOfMemory errors.")
        
        #obj = ScraperStat.objects.all().order_by('-import_corps_finish')[0]
        #importPeopleStartDate = datetime.datetime.now()

        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.AFFILIATION_DATA), encoding="utf-8-sig") as affiliation_file:
            print("Loading people")
            people.load_people_from_affiliations(affiliation_file)
        dates = None
        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.DATE_DATA),encoding="utf-8-sig") as dates_file:
            print("Loading statement dates")
            dates = people.load_doc_dates(dates_file)
        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.AFFILIATION_DATA), encoding="utf-8-sig") as affiliation_file:
            print("Loading affiliations")
            people.load_affiliations(affiliation_file,dates)

        #importPeopleFinishDate = datetime.datetime.now()
        #obj.import_people_start = importPeopleStartDate
        #obj.import_people_finish = importPeopleFinishDate 
        #obj.save()
        