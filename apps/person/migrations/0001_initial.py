# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=200, null=True, blank=True)),
                ('cite_type', models.CharField(max_length=100)),
                ('cite_link', models.URLField()),
                ('valid_date', models.DateField(null=True, blank=True)),
                ('share', models.FloatField(null=True, blank=True)),
                ('corp', models.ForeignKey(to='corporations.Corporation')),
            ],
            options={
                'get_latest_by': 'valid_date',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=500, null=True, blank=True)),
                ('personal_code', models.CharField(max_length=200, db_index=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('nationality', models.CharField(max_length=200, null=True, blank=True)),
                ('no_index_tag', models.NullBooleanField()),
                ('affiliations', models.ManyToManyField(to='corporations.Corporation', null=True, through='person.Affiliation', blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='person',
            field=models.ForeignKey(to='person.Person'),
            preserve_default=True,
        ),
    ]
