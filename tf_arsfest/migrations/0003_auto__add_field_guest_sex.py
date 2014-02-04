# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guest.sex'
        db.add_column('tf_arsfest_guest', 'sex',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guest.sex'
        db.delete_column('tf_arsfest_guest', 'sex')


    models = {
        'tf_arsfest.event': {
            'Meta': {'object_name': 'Event'},
            'alcohol_price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'places': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'registration_description': ('django.db.models.fields.TextField', [], {}),
            'round1_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'round1_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'round2_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'round2_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'silliz_price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'})
        },
        'tf_arsfest.guest': {
            'Meta': {'object_name': 'Guest'},
            'allergies': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tf_arsfest.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'nonalcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'silliz': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tf_arsfest.GuestType']"})
        },
        'tf_arsfest.guesttype': {
            'Meta': {'object_name': 'GuestType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'tf_arsfest.registration': {
            'Meta': {'object_name': 'Registration'},
            'avec': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'avec'", 'unique': 'True', 'null': 'True', 'to': "orm['tf_arsfest.Guest']"}),
            'avecbutton': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tf_arsfest.Event']"}),
            'greeting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'guest': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'guest'", 'unique': 'True', 'to': "orm['tf_arsfest.Guest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'misc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'plusone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reference_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'solennakt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sum': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tf_arsfest']