# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Image'
        db.create_table('images_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('mod_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('images', ['Image'])


    def backwards(self, orm):
        
        # Deleting model 'Image'
        db.delete_table('images_image')


    models = {
        'images.image': {
            'Meta': {'ordering': "['-upload_date']", 'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['images']
