# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Item'
        db.create_table('items_item', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['categories.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('discount', self.gf('django.db.models.fields.FloatField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('is_sold', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('seller', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seller', to=orm['auth.User'])),
            ('buyer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='buyer', to=orm['auth.User'])),
            ('sell_type', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('publishing_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('condition', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('items', ['Item'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Item'
        db.delete_table('items_item')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 8, 3, 6, 54, 527716, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 8, 3, 6, 54, 527612, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'items.item': {
            'Meta': {'object_name': 'Item'},
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'buyer'", 'to': "orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.Category']"}),
            'condition': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'discount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_sold': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'publishing_date': ('django.db.models.fields.DateTimeField', [], {}),
            'sell_type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seller'", 'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['items']
