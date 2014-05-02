# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Resource.publish_date'
        db.add_column(u'content_submit_resource', 'publish_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 2, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Resource.publish_date'
        db.delete_column(u'content_submit_resource', 'publish_date')


    models = {
        u'content_submit.resource': {
            'Meta': {'object_name': 'Resource'},
            'category': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '220'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '220'})
        }
    }

    complete_apps = ['content_submit']