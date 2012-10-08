# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Ad'
        db.create_table('ads_ad', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('discount', self.gf('django.db.models.fields.FloatField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('ads', ['Ad'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Ad'
        db.delete_table('ads_ad')
    
    
    models = {
        'ads.ad': {
            'Meta': {'object_name': 'Ad'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'discount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['ads']
