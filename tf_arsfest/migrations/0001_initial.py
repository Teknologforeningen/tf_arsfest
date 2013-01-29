# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guest'
        db.create_table('tf_arsfest_guest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('allergies', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tf_arsfest.GuestType'])),
            ('nonalcoholic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('silliz', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tf_arsfest.Event'])),
        ))
        db.send_create_signal('tf_arsfest', ['Guest'])

        # Adding model 'Registration'
        db.create_table('tf_arsfest_registration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tf_arsfest.Event'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('solennakt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('greeting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('guest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='guest', unique=True, to=orm['tf_arsfest.Guest'])),
            ('avec', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='avec', unique=True, null=True, to=orm['tf_arsfest.Guest'])),
            ('misc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('avecbutton', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reference_number', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, null=True, blank=True)),
            ('sum', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('tf_arsfest', ['Registration'])

        # Adding model 'Event'
        db.create_table('tf_arsfest_event', (
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('places', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('round1_opens', self.gf('django.db.models.fields.DateTimeField')()),
            ('round1_closes', self.gf('django.db.models.fields.DateTimeField')()),
            ('round2_opens', self.gf('django.db.models.fields.DateTimeField')()),
            ('round2_closes', self.gf('django.db.models.fields.DateTimeField')()),
            ('registration_description', self.gf('django.db.models.fields.TextField')()),
            ('silliz_price', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('alcohol_price', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('tf_arsfest', ['Event'])

        # Adding model 'GuestType'
        db.create_table('tf_arsfest_guesttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('tf_arsfest', ['GuestType'])


    def backwards(self, orm):
        # Deleting model 'Guest'
        db.delete_table('tf_arsfest_guest')

        # Deleting model 'Registration'
        db.delete_table('tf_arsfest_registration')

        # Deleting model 'Event'
        db.delete_table('tf_arsfest_event')

        # Deleting model 'GuestType'
        db.delete_table('tf_arsfest_guesttype')


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
            'reference_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'solennakt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sum': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tf_arsfest']