# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table(u'content_submit_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=220)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.CharField')(default=None, max_length=220)),
        ))
        db.send_create_signal(u'content_submit', ['Resource'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table(u'content_submit_resource')


    models = {
        u'content_submit.resource': {
            'Meta': {'object_name': 'Resource'},
            'category': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '220'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '220'})
        }
    }

    complete_apps = ['content_submit']