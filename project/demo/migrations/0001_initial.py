# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DemoUser'
        db.create_table('demo_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('paycheck', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_joined', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'demo', ['DemoUser'])


    def backwards(self, orm):
        # Deleting model 'DemoUser'
        db.delete_table('demo_users')


    models = {
        u'demo.demouser': {
            'Meta': {'object_name': 'DemoUser', 'db_table': "'demo_users'"},
            'date_joined': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'paycheck': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['demo']