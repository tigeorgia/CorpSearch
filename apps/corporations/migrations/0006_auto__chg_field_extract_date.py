# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Extract.date'
        db.alter_column(u'corporations_extract', 'date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Extract.date'
        db.alter_column(u'corporations_extract', 'date', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'corporations.corporation': {
            'Meta': {'object_name': 'Corporation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {}),
            'registry_db_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state_reg_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'corporations.extract': {
            'Meta': {'object_name': 'Extract'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corporations.Corporation']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['corporations']