# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Post'
        db.create_table('posts_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('posts', ['Post'])


    def backwards(self, orm):
        
        # Deleting model 'Post'
        db.delete_table('posts_post')


    models = {
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['posts']
