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
    additional_fields = None

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
        for i, item in enumerate(context[self.context_object_name]):
            data = model_to_dict(item)

            # Additional fields to include to the CSV (this should be a dict)
            if self.additional_fields:
                # Get all additional fields
                for k, v in self.additional_fields.iteritems():
                    attribute_value = getattr(item, k)
                    # if attribute value is a list, grab the first one
                    if isinstance(attribute_value, list):
                        attribute_value = attribute_value[0]

                    # Get final value of the attribute
                    for field_name in v:
                        final_value = getattr(attribute_value, field_name)
                        data[field_name] = final_value

            # For the header.
            if i == 0:
                dd = [unicode(k).encode('utf-8') for k in data.keys()]
                writer.writerow([unicode(k).encode('utf-8') for k in data.keys()])
            writer.writerow([unicode(data[k]).encode('utf-8') for k in data])

