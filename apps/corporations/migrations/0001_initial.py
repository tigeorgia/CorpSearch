# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_code', models.CharField(db_index=True, max_length=50, null=True, blank=True)),
                ('personal_code', models.CharField(max_length=100, null=True, blank=True)),
                ('state_reg_code', models.CharField(max_length=100, null=True, blank=True)),
                ('registry_db_code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=1000, db_index=True)),
                ('registration_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Extract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('email', models.CharField(max_length=750, null=True, blank=True)),
                ('corpurl', models.CharField(max_length=750, null=True, blank=True)),
                ('corp', models.ForeignKey(to='corporations.Corporation')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LegalFormLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='extract',
            name='legalform',
            field=models.ForeignKey(blank=True, to='corporations.LegalFormLookup', null=True),
            preserve_default=True,
        ),
    ]
