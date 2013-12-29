# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DemoUser.paycheck'
        db.alter_column('demo_users', 'paycheck', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DemoUser.date_joined'
        db.alter_column('demo_users', 'date_joined', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'DemoUser.paycheck'
        db.alter_column('demo_users', 'paycheck', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DemoUser.date_joined'
        db.alter_column('demo_users', 'date_joined', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'demo.demouser': {
            'Meta': {'object_name': 'DemoUser', 'db_table': "'demo_users'"},
            'date_joined': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['demo']