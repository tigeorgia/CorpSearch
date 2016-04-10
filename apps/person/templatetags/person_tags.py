from django import template
register = template.Library()

@register.simple_tag
def percentage(value):
    return "{:.2%}".format(value) if value else ""
