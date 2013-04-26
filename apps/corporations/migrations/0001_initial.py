# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Corporation'
        db.create_table(u'corporations_corporation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('personal_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('state_reg_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('registry_db_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('registration_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'corporations', ['Corporation'])


    def backwards(self, orm):
        # Deleting model 'Corporation'
        db.delete_table(u'corporations_corporation')


    models = {
        u'corporations.corporation': {
            'Meta': {'object_name': 'Corporation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {}),
            'registry_db_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state_reg_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['corporations']