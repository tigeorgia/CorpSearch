# -*- coding: utf-8 -*-
import json, codecs
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation, Extract
from apps.corporations.forms import ExtractForm

def load_extracts(infile):
    """ Adds extracts to the corresponding Corporations."""
    i = 0
    extracts = []
    for l in infile:
        if i % 1000 == 0:
            print i
        i += 1
        if i % 10000 == 0:
            print ("Loading a batch.")
            Extract.objects.bulk_create(extracts)
            extracts = []


        try:
            obj = json.loads(l)
        except ValueError as e:
            print u"Line:{}".format(l)
            #raise e
        remap = {"fk_corp_id_code": "corp",
                 "date": "date",
                 "corp_address": "address",
                 "corp_email": "email",}
        obj = {remap[key]: val for key, val in obj.items()}
        
        try:
            corp = Corporation.objects.get(id_code=obj['corp'])
        except (ObjectDoesNotExist, KeyError):
            continue
        obj['corp'] = corp.pk
        try:
            obj['date'] = _format_date(obj['date'])
        except KeyError:
            pass
        except ValueError:
            obj['date'] = None
        if ExtractForm(obj).is_valid():
            obj['corp'] = corp
            extracts.append(Extract(**obj))

    print("Loading the remainder.")
    Extract.objects.bulk_create(extracts)
def _format_date(string):
    return datetime.strptime(string, "%d/%m/%Y %H:%M:%S")#.strftime("%Y-%m-%d %H:%M:%S")
