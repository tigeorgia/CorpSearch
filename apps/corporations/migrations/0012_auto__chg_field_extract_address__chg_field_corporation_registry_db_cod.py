# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Extract.address'
        db.alter_column(u'corporations_extract', 'address', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Corporation.registry_db_code'
        db.alter_column(u'corporations_corporation', 'registry_db_code', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Corporation.name'
        db.alter_column(u'corporations_corporation', 'name', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Corporation.state_reg_code'
        db.alter_column(u'corporations_corporation', 'state_reg_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Corporation.personal_code'
        db.alter_column(u'corporations_corporation', 'personal_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Extract.address'
        db.alter_column(u'corporations_extract', 'address', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Corporation.registry_db_code'
        db.alter_column(u'corporations_corporation', 'registry_db_code', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Corporation.name'
        db.alter_column(u'corporations_corporation', 'name', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Corporation.state_reg_code'
        db.alter_column(u'corporations_corporation', 'state_reg_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Corporation.personal_code'
        db.alter_column(u'corporations_corporation', 'personal_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    models = {
        u'corporations.corporation': {
            'Meta': {'object_name': 'Corporation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'registry_db_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_reg_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'corporations.extract': {
            'Meta': {'object_name': 'Extract'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corporations.Corporation']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legalform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corporations.LegalFormLookup']", 'null': 'True', 'blank': 'True'})
        },
        u'corporations.legalformlookup': {
            'Meta': {'object_name': 'LegalFormLookup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['corporations']