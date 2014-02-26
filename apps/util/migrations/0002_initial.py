# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScraperStat'
        db.create_table(u'util_scraperstat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scrape_start', self.gf('django.db.models.fields.DateField')()),
            ('scrape_finish', self.gf('django.db.models.fields.DateField')()),
            ('import_start', self.gf('django.db.models.fields.DateField')()),
            ('import_finish', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'util', ['ScraperStat'])


    def backwards(self, orm):
        # Deleting model 'ScraperStat'
        db.delete_table(u'util_scraperstat')


    models = {
        u'util.scraperstat': {
            'Meta': {'object_name': 'ScraperStat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_finish': ('django.db.models.fields.DateField', [], {}),
            'import_start': ('django.db.models.fields.DateField', [], {}),
            'scrape_finish': ('django.db.models.fields.DateField', [], {}),
            'scrape_start': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['util']