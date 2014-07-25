# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BannedUser.tried_to_access'
        db.add_column(u'util_banneduser', 'tried_to_access',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BannedUser.tried_to_access'
        db.delete_column(u'util_banneduser', 'tried_to_access')


    models = {
        u'util.banneduser': {
            'Meta': {'object_name': 'BannedUser'},
            'ban_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39'}),
            'tried_to_access': ('django.db.models.fields.IntegerField', [], {})
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