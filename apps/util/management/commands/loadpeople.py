import codecs, os, sys

from django.core.management.base import BaseCommand, CommandError

import settings
from apps.corporations.load import corporations, extracts
from apps.corporations.models import Corporation, Extract
from apps.person.load import people
from apps.person.models import Person, Affiliation

class Command(BaseCommand):
    help = "Reloads data from the 'data' directory."

    AFFILIATION_DATA = "PersonCorpRelation.json"
    DATA_FOLDER = 'data'

    def handle(self, *args, **options):
        """ Loads new person data."""
        if settings.DEBUG == True:
            raise Exception("Please set settings.DEBUG to False unless you like OutOfMemory errors.")

        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.AFFILIATION_DATA), encoding="utf-8-sig") as affiliation_file:
            print("Loading people")
            people.load_people_from_affiliations(affiliation_file)
        with codecs.open(os.path.join(settings.PROJECT_PATH,self.DATA_FOLDER,self.AFFILIATION_DATA), encoding="utf-8-sig") as affiliation_file:
            print("Loading affiliations")
            people.load_affiliations(affiliation_file)
