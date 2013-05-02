import codecs, os, sys

from django.core.management.base import BaseCommand, CommandError

import settings
from apps.corporations.load import corporations, extracts
from apps.corporations.models import Corporation, Extract
from apps.person.load import people
from apps.person.models import Person, Affiliation

class Command(BaseCommand):
    help = "Deletes existing data."

    def handle(self, *args, **options):
        """ Clears the database, then loads new data."""
        _reset_data()

def _reset_data():
    # Reset stdout to capture django-admin command output
    print("Resetting corporations")
    Extract.objects.all().delete()
    Corporation.objects.all().delete()
