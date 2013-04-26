# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'person_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('personal_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'person', ['Person'])

        # Adding model 'Affiliation'
        db.create_table(u'person_affiliation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'])),
            ('corp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corporations.Corporation'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cite_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cite_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('is_ongoing', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'person', ['Affiliation'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'person_person')

        # Deleting model 'Affiliation'
        db.delete_table(u'person_affiliation')


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
        },
        u'person.affiliation': {
            'Meta': {'object_name': 'Affiliation'},
            'cite_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'cite_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corporations.Corporation']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ongoing': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['person.Person']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corporations.Corporation']", 'through': u"orm['person.Affiliation']", 'symmetrical': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'personal_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['person']