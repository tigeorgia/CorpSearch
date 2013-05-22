from django.http import HttpResponse
from django.forms.models import model_to_dict
import csv
import codecs
# Create your views here.
class CsvResponseMixin(object):
    """
    A mixin that can be used to render a CSV response.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a CSV response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'text/csv'
        response = self.response_class(**response_kwargs)
        response['Content-Disposition'] = 'attachment; filename="data.csv"'


        self.write_context_to_response(context,response)

        return response

    def write_context_to_response(self, context,response):
        "Convert the context dictionary into CSV rows"
        response.write(codecs.BOM_UTF8)
        writer = csv.writer(response)
        for item in context[self.context_object_name]:
            data = model_to_dict(item)
            writer.writerow([unicode(data[k]).encode('utf-8') for k in data])

