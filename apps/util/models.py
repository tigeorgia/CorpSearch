from django.db import models
import datetime


class ScraperStat(models.Model):
    import_corps_start = models.DateTimeField(editable=True, null=True)
    import_corps_finish = models.DateTimeField(editable=True, null=True)
    import_people_start = models.DateTimeField(editable=True, null=True)
    import_people_finish = models.DateTimeField(editable=True, null=True)


class BannedUser(models.Model):
    TIME_CHOICES = (
        (datetime.datetime.now() + datetime.timedelta(days=1), "1 Day"),
        (datetime.datetime.now() + datetime.timedelta(days=5), "5 Days"),
        (datetime.datetime.now() + datetime.timedelta(days=30), "30 Days"),
        (datetime.datetime.max, "Permanent")
    )

    ip = models.GenericIPAddressField("ip address", null=False, blank=False, unique=True)
    ban_time = models.DateTimeField(choices=TIME_CHOICES, null=False, blank=False)
    tried_to_access = models.IntegerField(default=0)

    @property
    def is_banned(self):
        """
        Checks if user is still banned and removes model if not anymore.
        @return: Banned status
        @rtype: bool
        """
        if datetime.datetime.now() < self.ban_time:
            return True
        else:
            self.delete()
            return False

    def __unicode__(self):
        return self.ip

