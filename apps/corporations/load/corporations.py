# -*- coding: utf-8 -*-
import json

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation
from apps.corporations.forms import CorporationForm
from apps.util.glt import month_ka2en
import codecs
from datetime import datetime

@transaction.commit_on_success
def load_corporations(infile):
    """ Inserts the corporations specified in infile into the
    database. Checks for duplicates. Requires a file buffer."""

    i = 0
    for l in infile:
        if i % 1000 == 0:
            print i
        i += 1
        corp = parse_corp(l)
        if corp is None:
            continue
        try: # Avoid duplicates
            Corporation.objects.get(id_code=corp.id_code)
        except ObjectDoesNotExist: #TODO: Merge
            corp.save()

def parse_corp(corp_string):
    """ Takes a string which is a single JSON object, and constructs a
    Corporation from the object."""

    data = json.loads(corp_string)
    corp = Corporation()
    remap = {"name": "name",
             "id_code_legal": "id_code",
             "personal_code": "personal_code",
             "state_reg_code": "state_reg_code",
             "id_code_reestri_db": "registry_db_code",
             "registration_date": "registration_date"}
    obj = {}
    for key, val in data.items():
        try:
            obj[remap[key]] = val
            
        except KeyError:
            pass

    try:
        date_geo = obj["registration_date"]
        date_eng = month_ka2en(date_geo)
        if date_eng != u"":
            date = datetime.strptime(date_eng,"%d %B %Y")
            obj["registration_date"] = date
    except KeyError:
        pass

    if CorporationForm(obj).is_valid():
        return Corporation(**obj)
    else:
        return None
