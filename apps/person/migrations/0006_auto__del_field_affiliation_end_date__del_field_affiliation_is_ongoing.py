# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Affiliation.end_date'
        db.delete_column(u'person_affiliation', 'end_date')

        # Deleting field 'Affiliation.is_ongoing'
        db.delete_column(u'person_affiliation', 'is_ongoing')

        # Deleting field 'Affiliation.start_date'
        db.delete_column(u'person_affiliation', 'start_date')

        # Adding field 'Affiliation.valid_date'
        db.add_column(u'person_affiliation', 'valid_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Affiliation.end_date'
        db.add_column(u'person_affiliation', 'end_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Affiliation.is_ongoing'
        db.add_column(u'person_affiliation', 'is_ongoing',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Affiliation.start_date'
        db.add_column(u'person_affiliation', 'start_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Affiliation.valid_date'
        db.delete_column(u'person_affiliation', 'valid_date')


    models = {
        u'corporations.corporation': {
            'Meta': {'object_name': 'Corporation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'registry_db_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state_reg_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['corporations.Corporation']", 'null': 'True', 'through': u"orm['person.Affiliation']", 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['person']