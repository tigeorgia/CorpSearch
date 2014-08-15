# -*- coding: utf-8 -*-
import json, codecs
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from apps.corporations.models import Corporation, Extract, LegalFormLookup
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
                 "corp_email": "email",
                 "corp_legalform": "legalform",
                 "corp_url": "corpurl"}
        obj = {remap[key]: val for key, val in obj.items()}
        
        if ("corpurl" not in obj):
            obj.pop('corpurl',None)
        
        legalform = None
        try:
            corp = Corporation.objects.get(id_code=obj['corp'])
        except (ObjectDoesNotExist, KeyError):
            continue
        obj['corp'] = corp.pk

        try:
            legalform_name = obj['legalform'].encode('utf8')
            if legalform_name:
                if legalform_name == 'შეზღუდული პასუხისმგებლობის საზოგადოება':
                    legalform_name = u'შპს'
                if legalform_name == 'სოლიდარული პასუხისმგებლობის საზოგადოება':
                    legalform_name = u'სპს'
            try:
                legalform = LegalFormLookup.objects.get(name=legalform_name)
                #obj['legalform'] = legalform
                obj['legalform'] = None
            except (ObjectDoesNotExist, KeyError):
                obj['legalform'] = None
        except (ObjectDoesNotExist, KeyError):
            pass

        if 'email' not in obj:
            obj['email'] = ''

        try:
            obj['date'] = _format_date(obj['date'])
        except KeyError:
            pass
        except ValueError:
            obj['date'] = None

        extract_form = ExtractForm(obj)
        if extract_form.is_valid():
            obj['corp'] = corp
            obj['legalform'] = legalform
            
            try:
                existingExtracts = Extract.objects.filter(corp_id=obj['corp'],email=obj['email'],address=obj['address']);
                if (len(existingExtracts) == 0):
                    extracts.append(Extract(**obj))
            except (ObjectDoesNotExist, KeyError):
                extracts.append(Extract(**obj))
        else:
            print extract_form.errors
        print i
        
    print("Loading the remainder.")
    Extract.objects.bulk_create(extracts)

def _format_date(string):
    return datetime.strptime(string, "%d/%m/%Y %H:%M:%S")#.strftime("%Y-%m-%d %H:%M:%S")
