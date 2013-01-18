# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participant'
        db.create_table('tf_arsfest_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('allergies', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tf_arsfest.ParticipantType'])),
            ('avec', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tf_arsfest.Participant'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('tf_arsfest', ['Participant'])

        # Adding model 'Event'
        db.create_table('tf_arsfest_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.TimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('tf_arsfest', ['Event'])

        # Adding model 'ParticipantType'
        db.create_table('tf_arsfest_participanttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('tf_arsfest', ['ParticipantType'])

        # Adding model 'Invoice'
        db.create_table('tf_arsfest_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('sum', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tf_arsfest', ['Invoice'])


    def backwards(self, orm):
        # Deleting model 'Participant'
        db.delete_table('tf_arsfest_participant')

        # Deleting model 'Event'
        db.delete_table('tf_arsfest_event')

        # Deleting model 'ParticipantType'
        db.delete_table('tf_arsfest_participanttype')

        # Deleting model 'Invoice'
        db.delete_table('tf_arsfest_invoice')


    models = {
        'tf_arsfest.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'tf_arsfest.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sum': ('django.db.models.fields.FloatField', [], {})
        },
        'tf_arsfest.participant': {
            'Meta': {'object_name': 'Participant'},
            'allergies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'avec': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tf_arsfest.Participant']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tf_arsfest.ParticipantType']"})
        },
        'tf_arsfest.participanttype': {
            'Meta': {'object_name': 'ParticipantType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['tf_arsfest']