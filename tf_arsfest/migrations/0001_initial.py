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
            ('allergies', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tf_arsfest.GuestType'])),
            ('nonalcoholic', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tf_arsfest', ['Guest'])

        # Adding model 'Registration'
        db.create_table('tf_arsfest_registration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('solennakt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('greeting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('guest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='guest', unique=True, to=orm['tf_arsfest.Guest'])),
            ('avec', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='avec', unique=True, null=True, to=orm['tf_arsfest.Guest'])),
            ('avecbutton', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tf_arsfest', ['Registration'])

        # Adding model 'Event'
        db.create_table('tf_arsfest_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.TimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('places', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('tf_arsfest', ['Event'])

        # Adding model 'GuestType'
        db.create_table('tf_arsfest_guesttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('tf_arsfest', ['GuestType'])

        # Adding model 'Invoice'
        db.create_table('tf_arsfest_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('sum', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tf_arsfest', ['Invoice'])


    def backwards(self, orm):
        # Deleting model 'Guest'
        db.delete_table('tf_arsfest_guest')

        # Deleting model 'Registration'
        db.delete_table('tf_arsfest_registration')

        # Deleting model 'Event'
        db.delete_table('tf_arsfest_event')

        # Deleting model 'GuestType'
        db.delete_table('tf_arsfest_guesttype')

        # Deleting model 'Invoice'
        db.delete_table('tf_arsfest_invoice')


    models = {
        'tf_arsfest.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'places': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'tf_arsfest.guest': {
            'Meta': {'object_name': 'Guest'},
            'allergies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'nonalcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tf_arsfest.GuestType']"})
        },
        'tf_arsfest.guesttype': {
            'Meta': {'object_name': 'GuestType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'tf_arsfest.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sum': ('django.db.models.fields.FloatField', [], {})
        },
        'tf_arsfest.registration': {
            'Meta': {'object_name': 'Registration'},
            'avec': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'avec'", 'unique': 'True', 'null': 'True', 'to': "orm['tf_arsfest.Guest']"}),
            'avecbutton': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'greeting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'guest': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'guest'", 'unique': 'True', 'to': "orm['tf_arsfest.Guest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'solennakt': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['tf_arsfest']