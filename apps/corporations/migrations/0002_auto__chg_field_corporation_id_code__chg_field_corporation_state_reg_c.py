# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Corporation.id_code'
        db.alter_column(u'corporations_corporation', 'id_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Corporation.state_reg_code'
        db.alter_column(u'corporations_corporation', 'state_reg_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Corporation.personal_code'
        db.alter_column(u'corporations_corporation', 'personal_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'Corporation.id_code'
        db.alter_column(u'corporations_corporation', 'id_code', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Corporation.state_reg_code'
        db.alter_column(u'corporations_corporation', 'state_reg_code', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Corporation.personal_code'
        db.alter_column(u'corporations_corporation', 'personal_code', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    models = {
        u'corporations.corporation': {
            'Meta': {'object_name': 'Corporation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {}),
            'registry_db_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state_reg_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['corporations']