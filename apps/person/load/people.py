# -*- coding: utf-8 -*-
import json
import codecs

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation
from apps.person.models import Person, Affiliation
from apps.person.forms import PersonForm, AffiliationForm
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

def load_affiliations(infile):
    """ Creates affiliations from an array of JSON objects. Requires 
    corporation and person tables to be populated."""
    i = 0
    #h = hpy()
    affiliations = []
    for l in infile:
        obj = json.loads(l)
        if i % 1000 == 0:
            print i
        if i % 10000 == 0:
            # Affiliation objects are large because they contain
            # both a Corporation and a Person object.
            # So flush the array every 10000 items to keep memory usage
            # reasonable.
            print("Saving past 10,000ish")
            Affiliation.objects.bulk_create(affiliations)
            affiliations = []
            #print h.heap()
        i += 1
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
                 "cite_link": "cite_link"}

        attrs = {remap[key]: val for key, val in obj.items()}
        attrs["corp"] = corp.pk
        attrs["person"] = pers.pk
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
    Affiliation.objects.bulk_create(affiliations)


def parse_person(json_string):
    """ Takes a json object and converts it into a Person object."""
    data = json.loads(corp_string)
    # Keys are identical in scrapy and Django, and no processing needed
    return Person(**data)
