# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneduser',
            name='ban_time',
            field=models.DateTimeField(choices=[(datetime.datetime(2015, 1, 31, 14, 35, 41, 168737), b'1 Day'), (datetime.datetime(2015, 2, 4, 14, 35, 41, 168760), b'5 Days'), (datetime.datetime(2015, 3, 1, 14, 35, 41, 168765), b'30 Days'), (datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), b'Permanent')]),
            preserve_default=True,
        ),
    ]
