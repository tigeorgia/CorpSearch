from django.db import models


class ScraperStat(models.Model):
    import_corps_start = models.DateTimeField(editable=True,null=True)
    import_corps_finish = models.DateTimeField(editable=True,null=True)
    import_people_start = models.DateTimeField(editable=True,null=True)
    import_people_finish = models.DateTimeField(editable=True,null=True)
    