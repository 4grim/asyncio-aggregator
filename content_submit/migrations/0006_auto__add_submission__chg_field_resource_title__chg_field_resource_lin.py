# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Submission'
        db.create_table(u'content_submit_submission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal(u'content_submit', ['Submission'])


        # Changing field 'Resource.title'
        db.alter_column(u'content_submit_resource', 'title', self.gf('django.db.models.fields.CharField')(max_length=254))

        # Changing field 'Resource.link'
        db.alter_column(u'content_submit_resource', 'link', self.gf('django.db.models.fields.URLField')(max_length=254))

    def backwards(self, orm):
        # Deleting model 'Submission'
        db.delete_table(u'content_submit_submission')


        # Changing field 'Resource.title'
        db.alter_column(u'content_submit_resource', 'title', self.gf('django.db.models.fields.CharField')(max_length=220))

        # Changing field 'Resource.link'
        db.alter_column(u'content_submit_resource', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'content_submit.resource': {
            'Meta': {'object_name': 'Resource'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '220'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '254'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'content_submit.submission': {
            'Meta': {'object_name': 'Submission'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '254'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['content_submit']