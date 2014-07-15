# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BannedUser'
        db.create_table(u'util_banneduser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(unique=True, max_length=39)),
            ('ban_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'util', ['BannedUser'])


    def backwards(self, orm):
        # Deleting model 'BannedUser'
        db.delete_table(u'util_banneduser')


    models = {
        u'util.banneduser': {
            'Meta': {'object_name': 'BannedUser'},
            'ban_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39'})
        },
        u'util.scraperstat': {
            'Meta': {'object_name': 'ScraperStat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_corps_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'import_corps_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'import_people_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'import_people_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['util']