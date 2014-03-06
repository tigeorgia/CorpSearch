from django import template
register = template.Library()

@register.simple_tag
def percentage(value):
    result = ""
    if value:
        result = "{0:.2f}%".format(value * 100)
    return result
    