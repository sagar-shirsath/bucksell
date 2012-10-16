from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    condition = models.PositiveIntegerField(max_length=1)
    price = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.TextField()
    buyer = models.ForeignKey(User , related_name="buyer" )
    seller = models.ForeignKey(User , related_name="seller" )
    discount = models.FloatField(default=0)
    sell_type = models.PositiveIntegerField(default=1)
    publishing_date = models.DateTimeField(datetime.now())
    category = models.ForeignKey(Category)
    is_published = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    slug = models.CharField(max_length=60)

    def saveFields(self,data):
        print(data['name'])
        if self.create(
                name=data['name'],
                description =data['description'],
                condition=data['condition'],
                price=data['price'],
                longitude =data['longitude'],
                latitude=data['latitude'],
                seller =data['seller']
            ):
            return True
        else:
            return False




class ItemPhoto():
    item = models.ForeignKey(Item)
    photo = models.ImageField(upload_to='images/items/')
    photo1 = models.ImageField(upload_to='images/items/')
    photo2 = models.ImageField(upload_to='images/items/')
    photo3 = models.ImageField(upload_to='images/items/')
    feedback_photo = models.ImageField(upload_to='images/items/')
    thumbnail = models.ImageField(upload_to='images/items/thumbnails')
    thumbnail1 = models.ImageField(upload_to='images/items/thumbnails')
    thumbnail2 = models.ImageField(upload_to='images/items/thumbnails')
    thumbnail3 = models.ImageField(upload_to='images/items/thumbnails')


