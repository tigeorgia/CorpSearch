# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ScraperStat.scrape_start'
        db.delete_column(u'util_scraperstat', 'scrape_start')

        # Deleting field 'ScraperStat.scrape_finish'
        db.delete_column(u'util_scraperstat', 'scrape_finish')

        # Adding field 'ScraperStat.scrape_corps_start'
        db.add_column(u'util_scraperstat', 'scrape_corps_start',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'ScraperStat.scrape_corps_finish'
        db.add_column(u'util_scraperstat', 'scrape_corps_finish',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'ScraperStat.scrape_people_start'
        db.add_column(u'util_scraperstat', 'scrape_people_start',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'ScraperStat.scrape_people_finish'
        db.add_column(u'util_scraperstat', 'scrape_people_finish',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


        # Changing field 'ScraperStat.import_start'
        db.alter_column(u'util_scraperstat', 'import_start', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ScraperStat.import_finish'
        db.alter_column(u'util_scraperstat', 'import_finish', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Adding field 'ScraperStat.scrape_start'
        db.add_column(u'util_scraperstat', 'scrape_start',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 26, 0, 0)),
                      keep_default=False)

        # Adding field 'ScraperStat.scrape_finish'
        db.add_column(u'util_scraperstat', 'scrape_finish',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 26, 0, 0)),
                      keep_default=False)

        # Deleting field 'ScraperStat.scrape_corps_start'
        db.delete_column(u'util_scraperstat', 'scrape_corps_start')

        # Deleting field 'ScraperStat.scrape_corps_finish'
        db.delete_column(u'util_scraperstat', 'scrape_corps_finish')

        # Deleting field 'ScraperStat.scrape_people_start'
        db.delete_column(u'util_scraperstat', 'scrape_people_start')

        # Deleting field 'ScraperStat.scrape_people_finish'
        db.delete_column(u'util_scraperstat', 'scrape_people_finish')


        # Changing field 'ScraperStat.import_start'
        db.alter_column(u'util_scraperstat', 'import_start', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 26, 0, 0)))

        # Changing field 'ScraperStat.import_finish'
        db.alter_column(u'util_scraperstat', 'import_finish', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 26, 0, 0)))

    models = {
        u'util.scraperstat': {
            'Meta': {'object_name': 'ScraperStat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_finish': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'import_start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'scrape_corps_finish': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'scrape_corps_start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'scrape_people_finish': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'scrape_people_start': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['util']