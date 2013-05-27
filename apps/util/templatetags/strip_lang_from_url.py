from django import template 
register = template.Library()

@register.simple_tag(takes_context=True)
def strip_lang_from_url(context):
    request=context.get('request',False)
    if not request:
        return None

    request=context['request']
    curr_url=request.path
    if len(curr_url) < 4 or curr_url[0] != '/' or curr_url[3] != '/':
        return curr_url

    #changed_url = '/'+lang_code+curr_url[3:]
    changed_url = curr_url[3:]
    return changed_url
