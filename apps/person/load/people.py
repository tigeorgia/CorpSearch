# -*- coding: utf-8 -*-
import json
import codecs
from datetime import datetime

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation
from apps.person.models import Person, Affiliation
from apps.person.forms import PersonForm, AffiliationForm
from apps.util.glt import month_ka2en
@transaction.commit_on_success
def load_people_from_affiliations(infile):
    """ Loads a set of Person-Corp relations, and creates Person objects from
    them. Checks for pre-existing Persons.
    Returns an array of affiliation objects parsed from JSON for use in
    loading affiliations. """
    objects = []
    i = 0
    for l in infile:
        if i % 1000 == 0:
            print i
        i += 1
        data = json.loads(l)
        if PersonForm(data['person']).is_valid():
            pers = Person(**data['person'])
            try:
                Person.objects.get(personal_code=pers.personal_code)
            except ObjectDoesNotExist: #TODO: Merge person data
                pers.save()

def load_affiliations(infile,dates):
    """ Creates affiliations from an array of JSON objects. Requires 
    corporation and person tables to be populated."""
    i = 0
    #h = hpy()
    affiliations = []
    for l in infile:
        obj = json.loads(l)
        if i % 1000 == 0:
            print i
        i += 1
        if i % 10000 == 0:
            # Affiliation objects are large because they contain
            # both a Corporation and a Person object.
            # So flush the array every 10000 items to keep memory usage
            # reasonable.
            print("Saving past 10,000ish")
            Affiliation.objects.bulk_create(affiliations)
            affiliations = []
            #print h.heap()
        try:
            pers = Person.objects.get(personal_code=obj['person']['personal_code'])
            corp = Corporation.objects.get(id_code=obj['fk_corp_id_code'])
        except KeyError:
            continue
        except ObjectDoesNotExist:
            continue
        remap = {"fk_corp_id_code": "corp",
                 "relation_type": "role",
                 "person": "person",
                 "cite_type": "cite_type",
                 "cite_link": "cite_link",
                 "share": "share",}

        attrs = {remap[key]: val for key, val in obj.items()}
        if "share" in obj:
            attrs["share"] = obj["share"]
            try:
                attrs["share"] = percent_to_float(attrs["share"])
            except ValueError:
                attrs["share"] = None
        else:
            attrs["share"] = None
        attrs["corp"] = corp.pk
        attrs["person"] = pers.pk
        try:
            attrs["valid_date"] = dates[attrs["cite_link"]]
        except KeyError:
            pass
        try:
            for role in obj['relation_type']:
                attrs["role"] = role
                if AffiliationForm(attrs).is_valid():
                    attrs["corp"] = corp
                    attrs["person"] = pers
                    affil = Affiliation(**attrs)
                    attrs["corp"] = corp.pk
                    attrs["person"] = pers.pk

                    affiliations.append(affil)
        except KeyError:
            if AffiliationForm(attrs).is_valid():
                attrs["corp"] = corp
                attrs["person"] = pers
                affil = Affiliation(**attrs)
                affiliations.append(affil)
                #affil.save()
        #print("Date: {}".format(affil.valid_date))
    print("Finished; loading remainder...")
    Affiliation.objects.bulk_create(affiliations)

def load_doc_dates(infile):
    """ Returns a dict of URL: date pairs, which will be used to apply
    dates to each recorded affiliation."""
    dates = {} # Will store URL: date pairs
    i = 0
    for docstr in infile:
        if i % 10000 == 0:
            print i
        i += 1
        obj = json.loads(docstr)
        try:
            date_geo = obj["date"]
            date_eng = month_ka2en(date_geo)
            if date_eng != u"":
                dates[obj["link"]] = datetime.strptime(date_eng,"%d %B %Y %H:%M")
        except KeyError:
            pass
    return dates

        
def percent_to_float(string):
    return float(string.strip("% "))/100

def parse_person(json_string):
    """ Takes a json object and converts it into a Person object."""
    data = json.loads(corp_string)
    # Keys are identical in scrapy and Django, and no processing needed
    return Person(**data)
