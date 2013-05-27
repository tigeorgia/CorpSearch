# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def ka_translit(value,arg):
    """ Returns the passed Georgian string as transliterated into the language
    given in arg."""
    if arg[0:2] in latin_langs:
        return value.translate(CHARMAP_GEO2LAT)
    return value
    
CHARMAP_GEO2LAT = {
    ord(u'ა'): u'a', ord(u'ბ'): u'b', ord(u'გ'): u'g', 
    ord(u'დ'): u'd', ord(u'ე'): u'e', ord(u'ვ'): u'v', 
    ord(u'ზ'): u'z', ord(u'თ'): u't', ord(u'ი'): u'i', 
    ord(u'კ'): u'k', ord(u'ქ'): u'k', ord(u'ლ'): u'l', 
    ord(u'მ'): u'm', ord(u'ნ'): u'n', ord(u'ო'): u'o',
    ord(u'პ'): u'p', ord(u'ჟ'): u'zh', ord(u'რ'): u'r', 
    ord(u'ს'): u's', ord(u'ტ'): u't', ord(u'უ'): u'u', 
    ord(u'ფ'): u'p', ord(u'ღ'): u'gh', ord(u'ყ'): u'q', 
    ord(u'შ'): u'sh', ord(u'ჩ'): u'ch', ord(u'ც'): u'ts', 
    ord(u'ძ'): u'dz', ord(u'წ'): u'ts', ord(u'ჭ'): u'ch', 
    ord(u'ხ'): u'kh', ord(u'ჯ'): u'j', ord(u'ჰ'): u'h',
}

latin_langs = ("en","de")
