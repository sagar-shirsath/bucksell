# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'PaymentType'
        db.create_table('transactions_paymenttype', (
            ('service_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('transaction_charge', self.gf('django.db.models.fields.FloatField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('transactions', ['PaymentType'])

        # Adding model 'Transaction'
        db.create_table('transactions_transaction', (
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('texes', self.gf('django.db.models.fields.FloatField')()),
            ('discount', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=2)),
            ('transaction_charge', self.gf('django.db.models.fields.FloatField')()),
            ('gross_amount', self.gf('django.db.models.fields.FloatField')()),
            ('net_revenue', self.gf('django.db.models.fields.FloatField')()),
            ('seller', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seller_user', to=orm['auth.User'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.Item'])),
            ('payment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.PaymentType'])),
            ('buyer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='buyer_user', to=orm['auth.User'])),
            ('discount_revenue', self.gf('django.db.models.fields.FloatField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('transactions', ['Transaction'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'PaymentType'
        db.delete_table('transactions_paymenttype')

        # Deleting model 'Transaction'
        db.delete_table('transactions_transaction')
    
    
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 8, 3, 17, 20, 187227)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 8, 3, 17, 20, 187120)'}),
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
        },
        'transactions.paymenttype': {
            'Meta': {'object_name': 'PaymentType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'service_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'transaction_charge': ('django.db.models.fields.FloatField', [], {})
        },
        'transactions.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'buyer_user'", 'to': "orm['auth.User']"}),
            'discount': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '2'}),
            'discount_revenue': ('django.db.models.fields.FloatField', [], {}),
            'gross_amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['items.Item']"}),
            'net_revenue': ('django.db.models.fields.FloatField', [], {}),
            'payment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['transactions.PaymentType']"}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seller_user'", 'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'texes': ('django.db.models.fields.FloatField', [], {}),
            'transaction_charge': ('django.db.models.fields.FloatField', [], {}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }
    
    complete_apps = ['transactions']
