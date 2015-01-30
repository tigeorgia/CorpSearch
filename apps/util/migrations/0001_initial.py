# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannedUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name=b'ip address')),
                ('ban_time', models.DateTimeField(choices=[(datetime.datetime(2015, 1, 31, 14, 34, 47, 179878), b'1 Day'), (datetime.datetime(2015, 2, 4, 14, 34, 47, 179927), b'5 Days'), (datetime.datetime(2015, 3, 1, 14, 34, 47, 179938), b'30 Days'), (datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), b'Permanent')])),
                ('tried_to_access', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScraperStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('import_corps_start', models.DateTimeField(null=True)),
                ('import_corps_finish', models.DateTimeField(null=True)),
                ('import_people_start', models.DateTimeField(null=True)),
                ('import_people_finish', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
