from django.db import models
from django.contrib.auth.models import User
from universities.modls import University
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    photo=models.ImageField(upload_to='imgaes/profiels')
    thumbnail = models.ImageField(upload_to="images/profiles/thumbnails")
    auth_token = models.CharField(max_length=20)
    fb_url = models.URLField(max_length=30)
    twitter_url = models.URLField(max_length=30)
    address = models.TextField()
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    university = models.ForeignKey(University)
    longitude = models.FloatField()
    latitude = models.FloatField()
    average_rating = models.PositiveIntegerField(default=0,max_length=1)
    paypal_url = models.CharField(max_length=50)
    interests = models.CharField(max_length=500)
    about_me = models.CharField(max_length=500)







