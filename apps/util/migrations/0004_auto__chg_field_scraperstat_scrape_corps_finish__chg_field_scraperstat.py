# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ScraperStat.scrape_corps_finish'
        db.alter_column(u'util_scraperstat', 'scrape_corps_finish', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'ScraperStat.import_start'
        db.alter_column(u'util_scraperstat', 'import_start', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'ScraperStat.scrape_people_finish'
        db.alter_column(u'util_scraperstat', 'scrape_people_finish', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'ScraperStat.scrape_corps_start'
        db.alter_column(u'util_scraperstat', 'scrape_corps_start', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'ScraperStat.import_finish'
        db.alter_column(u'util_scraperstat', 'import_finish', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'ScraperStat.scrape_people_start'
        db.alter_column(u'util_scraperstat', 'scrape_people_start', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'ScraperStat.scrape_corps_finish'
        db.alter_column(u'util_scraperstat', 'scrape_corps_finish', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ScraperStat.import_start'
        db.alter_column(u'util_scraperstat', 'import_start', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ScraperStat.scrape_people_finish'
        db.alter_column(u'util_scraperstat', 'scrape_people_finish', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ScraperStat.scrape_corps_start'
        db.alter_column(u'util_scraperstat', 'scrape_corps_start', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ScraperStat.import_finish'
        db.alter_column(u'util_scraperstat', 'import_finish', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ScraperStat.scrape_people_start'
        db.alter_column(u'util_scraperstat', 'scrape_people_start', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'util.scraperstat': {
            'Meta': {'object_name': 'ScraperStat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'import_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'scrape_corps_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'scrape_corps_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'scrape_people_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'scrape_people_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['util']