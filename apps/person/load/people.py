# -*- coding: utf-8 -*-
import json
import codecs

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation
from apps.person.models import Person, Affiliation

@transaction.commit_on_success
def load_people_from_relations(infile):
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
        pers = Person(**data['person'])
    
        try:
            Person.objects.get(personal_code=pers.personal_code)
        except ObjectDoesNotExist: #TODO: Merge person data
            pers.save()

        objects.append(data) # Come back to affiliations after people
    return objects

def load_affiliations(objects):
    """ Creates affiliations from an array of JSON objects. Requires 
    corporation and person tables to be populated."""
    i = 0
    affiliations = []
    for obj in objects:
        if i % 1000 == 0:
            print i
        i += 1
        try:
            pers = Person.objects.get(personal_code=obj['person']['personal_code'])
            corp = Corporation.objects.get(id_code=obj['fk_corp_id_code'])
        except KeyError:
            continue
        remap = {"fk_corp_id_code": "corp",
                 "relation_type": "role",
                 "person": "person",
                 "cite_type": "cite_type",
                 "cite_link": "cite_link"}

        attrs = {remap[key]: val for key, val in obj.items()}
        attrs["corp"] = corp
        attrs["person"] = pers
        try:
            for role in obj['relation_type']:
                attrs["role"] = role
                affil = Affiliation(**attrs)
                affiliations.append(affil)
        except KeyError:
            affil = Affiliation(**attrs)
            affiliations.append(affil)

    Affiliation.objects.bulk_create(affiliations)

def parse_person(json_string):
    """ Takes a json object and converts it into a Person object."""
    data = json.loads(corp_string)
    # Keys are identical in scrapy and Django, and no processing needed
    return Person(**data)
