# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'University.longitude'
        db.alter_column('universities_university', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'University.latitude'
        db.alter_column('universities_university', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'University.longitude'
        db.alter_column('universities_university', 'longitude', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'University.latitude'
        db.alter_column('universities_university', 'latitude', self.gf('django.db.models.fields.FloatField')())
    
    
    models = {
        'universities.university': {
            'Meta': {'object_name': 'University'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }
    
    complete_apps = ['universities']
