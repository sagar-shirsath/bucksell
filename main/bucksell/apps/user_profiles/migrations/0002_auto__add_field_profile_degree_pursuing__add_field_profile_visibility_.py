# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Profile.degree_pursuing'
        db.add_column('user_profiles_profile', 'degree_pursuing', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Profile.visibility'
        db.add_column('user_profiles_profile', 'visibility', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'Profile.gender'
        db.add_column('user_profiles_profile', 'gender', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'Profile.year_of_class'
        db.add_column('user_profiles_profile', 'year_of_class', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Changing field 'Profile.interests'
        db.alter_column('user_profiles_profile', 'interests', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Profile.phone_number'
        db.alter_column('user_profiles_profile', 'phone_number', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

        # Changing field 'Profile.fb_url'
        db.alter_column('user_profiles_profile', 'fb_url', self.gf('django.db.models.fields.URLField')(max_length=30, null=True))

        # Changing field 'Profile.city'
        db.alter_column('user_profiles_profile', 'city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Profile.twitter_url'
        db.alter_column('user_profiles_profile', 'twitter_url', self.gf('django.db.models.fields.URLField')(max_length=30, null=True))

        # Changing field 'Profile.paypal_url'
        db.alter_column('user_profiles_profile', 'paypal_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.auth_token'
        db.alter_column('user_profiles_profile', 'auth_token', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Profile.longitude'
        db.alter_column('user_profiles_profile', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Profile.about_me'
        db.alter_column('user_profiles_profile', 'about_me', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Profile.address'
        db.alter_column('user_profiles_profile', 'address', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Profile.latitude'
        db.alter_column('user_profiles_profile', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Profile.zip_code'
        db.alter_column('user_profiles_profile', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))
    
    
    def backwards(self, orm):
        
        # Deleting field 'Profile.degree_pursuing'
        db.delete_column('user_profiles_profile', 'degree_pursuing')

        # Deleting field 'Profile.visibility'
        db.delete_column('user_profiles_profile', 'visibility')

        # Deleting field 'Profile.gender'
        db.delete_column('user_profiles_profile', 'gender')

        # Deleting field 'Profile.year_of_class'
        db.delete_column('user_profiles_profile', 'year_of_class')

        # Changing field 'Profile.interests'
        db.alter_column('user_profiles_profile', 'interests', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Profile.phone_number'
        db.alter_column('user_profiles_profile', 'phone_number', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'Profile.fb_url'
        db.alter_column('user_profiles_profile', 'fb_url', self.gf('django.db.models.fields.URLField')(max_length=30))

        # Changing field 'Profile.city'
        db.alter_column('user_profiles_profile', 'city', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Profile.twitter_url'
        db.alter_column('user_profiles_profile', 'twitter_url', self.gf('django.db.models.fields.URLField')(max_length=30))

        # Changing field 'Profile.paypal_url'
        db.alter_column('user_profiles_profile', 'paypal_url', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Profile.auth_token'
        db.alter_column('user_profiles_profile', 'auth_token', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Profile.longitude'
        db.alter_column('user_profiles_profile', 'longitude', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Profile.about_me'
        db.alter_column('user_profiles_profile', 'about_me', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Profile.address'
        db.alter_column('user_profiles_profile', 'address', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Profile.latitude'
        db.alter_column('user_profiles_profile', 'latitude', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Profile.zip_code'
        db.alter_column('user_profiles_profile', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10))
    
    
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 1, 16, 7, 24, 448256)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 1, 16, 7, 24, 448125)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'universities.university': {
            'Meta': {'object_name': 'University'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'user_profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'auth_token': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'average_rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '1'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'degree_pursuing': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'fb_url': ('django.db.models.fields.URLField', [], {'max_length': '30', 'null': 'True'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'paypal_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100'}),
            'twitter_url': ('django.db.models.fields.URLField', [], {'max_length': '30', 'null': 'True'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['universities.University']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_userfk'", 'to': "orm['auth.User']"}),
            'visibility': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'year_of_class': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }
    
    complete_apps = ['user_profiles']
