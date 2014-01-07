# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DemoUser.date_free'
        db.delete_column(u'demo_demouser', 'date_free')


    def backwards(self, orm):
        # Adding field 'DemoUser.date_free'
        db.add_column(u'demo_demouser', 'date_free',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


    models = {
        u'demo.demouser': {
            'Meta': {'object_name': 'DemoUser'},
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