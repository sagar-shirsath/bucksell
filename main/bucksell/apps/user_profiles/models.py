from django.db import models
from django.contrib.auth.models import User
from universities.models import University
import datetime
import hashlib
import random
import re

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,related_name="auth_user")
    photo=models.ImageField(upload_to='images/profiles',default=None)
    thumbnail = models.ImageField(upload_to="images/profiles/thumbnails",default=None)
    auth_token = models.CharField(max_length=20,null=True)
    fb_url = models.URLField(max_length=30,null=True)
    twitter_url = models.URLField(max_length=30,null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=30,null=True)
    zip_code = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=12,null=True)
    university = models.ForeignKey(University,blank=True, null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    average_rating = models.PositiveIntegerField(default=0,max_length=1)
    paypal_url = models.CharField(max_length=50,null=True)
    interests = models.CharField(max_length=500,null=True)
    about_me = models.CharField(max_length=500,null=True)
    gender = models.PositiveSmallIntegerField(default=0)
    visibility = models.PositiveSmallIntegerField(default=0)
    year_of_class = models.PositiveIntegerField(default=0)
    degree_pursuing = models.CharField(max_length=200,null=True)

    def create_user_profile(self,user_id):
        profile =   Profile.objects.create(user_id=user_id)
        profile.save()
        return profile



