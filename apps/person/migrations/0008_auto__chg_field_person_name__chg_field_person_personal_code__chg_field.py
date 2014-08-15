# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.name'
        db.alter_column(u'person_person', 'name', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Person.personal_code'
        db.alter_column(u'person_person', 'personal_code', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Person.nationality'
        db.alter_column(u'person_person', 'nationality', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Person.name'
        db.alter_column(u'person_person', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Person.personal_code'
        db.alter_column(u'person_person', 'personal_code', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.nationality'
        db.alter_column(u'person_person', 'nationality', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        u'corporations.corporation': {
            'Meta': {'object_name': 'Corporation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'registry_db_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_reg_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'person.affiliation': {
            'Meta': {'object_name': 'Affiliation'},
            'cite_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'cite_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corporations.Corporation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['person.Person']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'share': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'valid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'affiliations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['corporations.Corporation']", 'null': 'True', 'through': u"orm['person.Affiliation']", 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['person']