# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DemoUser'
        db.create_table(u'demo_demouser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('paycheck', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_free', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'demo', ['DemoUser'])

        # Adding model 'Room'
        db.create_table(u'demo_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'demo', ['Room'])


    def backwards(self, orm):
        # Deleting model 'DemoUser'
        db.delete_table(u'demo_demouser')

        # Deleting model 'Room'
        db.delete_table(u'demo_room')


    models = {
        u'demo.demouser': {
            'Meta': {'object_name': 'DemoUser'},
            'date_free': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'demo.room': {
            'Meta': {'object_name': 'Room'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['demo']