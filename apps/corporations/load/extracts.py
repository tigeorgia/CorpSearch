# -*- coding: utf-8 -*-
import json
import codecs

from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation, Extract

def load_extracts(infile):
    """ Adds extracts to the corresponding Corporations."""
    extracts = []
    i = 0
    for l in infile:
        if i % 1000 == 0:
            print i
        i += 1

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
        obj['corp'] = corp
        extract = Extract(**obj)

    Extract.objects.bulk_create(extracts)
