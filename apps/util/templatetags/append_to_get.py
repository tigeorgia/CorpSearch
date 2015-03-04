from django import template
from django.utils.html import escape

register = template.Library()

"""
Decorator to facilitate template tag creation
"""
def easy_tag(func):
    """deal with the repetitive parts of parsing template tags"""
    def inner(parser, token):
        #print token
        try:
            return func(*token.split_contents())
        except TypeError:
            raise template.TemplateSyntaxError('Bad arguments for tag "%s"' % token.split_contents()[0])
    inner.__name__ = func.__name__
    inner.__doc__ = inner.__doc__
    return inner



class AppendGetNode(template.Node):
    def __init__(self, dict):
        self.dict_pairs = {}
        for pair in dict.split(','):
            pair = pair.split('=')
            self.dict_pairs[pair[0]] = template.Variable(pair[1])
            
    def render(self, context):
        get = context['request'].GET.copy()

        for key in self.dict_pairs:
            if (key == "order_by" and "order_by" in get):
                # Specific url parameter handeling, for column sorting on people result page
                value = self.dict_pairs[key].resolve(context)
                if value == get[key]:
                    if value.startswith("-"):
                        result = value[1:len(get[key])]
                    else:
                        result = "-"+value
                    get[key] = result
                else:
                    get[key] = self.dict_pairs[key].resolve(context)
            else:
                get[key] = self.dict_pairs[key].resolve(context)
                
        
        path = context['request'].META['PATH_INFO']
        
        #print "&".join(["%s=%s" % (key, value) for (key, value) in get.items() if value])
        
        if len(get):
            path += "?%s" % "&".join(["%s=%s" % (key, value) for (key, value) in get.items() if value])
        
        
        return escape(path)

@register.tag()
@easy_tag
def append_to_get(_tag_name, dict):
    return AppendGetNode(dict)
