# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participant'
        db.create_table('registration_app_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('allergies', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration_app.ParticipantType'])),
            ('avec', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration_app.Participant'], null=True, blank=True)),
        ))
        db.send_create_signal('registration_app', ['Participant'])

        # Adding model 'Event'
        db.create_table('registration_app_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.TimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('registration_app', ['Event'])

        # Adding model 'ParticipantType'
        db.create_table('registration_app_participanttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('registration_app', ['ParticipantType'])


    def backwards(self, orm):
        # Deleting model 'Participant'
        db.delete_table('registration_app_participant')

        # Deleting model 'Event'
        db.delete_table('registration_app_event')

        # Deleting model 'ParticipantType'
        db.delete_table('registration_app_participanttype')


    models = {
        'registration_app.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'registration_app.participant': {
            'Meta': {'object_name': 'Participant'},
            'allergies': ('django.db.models.fields.TextField', [], {}),
            'avec': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration_app.Participant']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration_app.ParticipantType']"})
        },
        'registration_app.participanttype': {
            'Meta': {'object_name': 'ParticipantType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['registration_app']