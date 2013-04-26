# -*- coding: utf-8 -*-
import json
from apps.corporations.models import Corporation
import codecs
import time

def load(infile):
    """ Inserts the corporations specified in infile into the
    database, without checking for duplicates. Good for loading initial
    data into the database."""
    ifile = codecs.open(infile, encoding="utf-8-sig")

    results = []
    for l in ifile:
        results.append(parse_corp(l))
    Corporation.objects.bulk_create(results)

def parse_corp(corp_string):
    """ Takes a string which is a single JSON object, and constructs a
    Corporation from the object."""

    data = json.loads(corp_string)
    corp = Corporation()
    # TODO: Make this not suck, move into custom init with field mappings.
    try:
        corp.name = data["name"]
    except KeyError:
        pass
    try:
        corp.id_code = data["id_code_legal"]
    except KeyError:
        pass
    try:
        corp.personal_code = data["personal_code"]
    except KeyError:
        pass
    try:
        corp.state_reg_code = data["state_reg_code"]
    except KeyError:
        pass
    try:
        corp.registry_db_code = data["id_code_reestri_db"]
    except KeyError:
        pass
    try:
        date_geo = data["registration_date"]
        date_eng = _substitute_date(date_geo)
        date = time.strptime(date_eng,"%d %B %Y")
        corp.registration_date = time.strftime("%Y-%m-%d",date)
    except KeyError:
        pass

    return corp

def _substitute_date(string):
    dates = [(u"January",u"იანვარი"),
             (u"February",u"თებერვალი"),
             (u"March",u"მარტი"),
             (u"April",u"აპრილი"),
             (u"May",u"მაისი"),
             (u"June",u"ივნისი"),
             (u"July",u"ივლისი"),
             (u"August",u"აგვისტო"),
             (u"September",u"სექტემბერი"),
             (u"October",u"ოქტომბერი"),
             (u"November",u"ნოემბერი"),
             (u"December",u"დეკემბერი")]
             
    for sub in dates:
        string = string.replace(sub[1],sub[0])

    return string
