from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import slugify
import random
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    condition = models.PositiveIntegerField(max_length=1)
    price = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.TextField()
    buyer = models.ForeignKey(User , related_name="buyer",null=True)
    seller = models.ForeignKey(User , related_name="seller" )
    discount = models.FloatField(default=0)
    sell_type = models.PositiveIntegerField(default=1)
    publishing_date = models.DateTimeField(default=datetime.now())
    category = models.ForeignKey(Category)
    is_published = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    slug = models.CharField(max_length=60)
    def save(self, *args, **kwargs):
        string = "%s-%s" % (random.randrange(0, 101, 2), self.name)
        self.slug = slugify(string)
        super(Item, self).save(*args, **kwargs)






class ItemPhoto():
    item = models.ForeignKey(Item)
    photo = models.ImageField(upload_to='images/items/',null=True)
    photo1 = models.ImageField(upload_to='images/items/',null=True)
    photo2 = models.ImageField(upload_to='images/items/',null=True)
    photo3 = models.ImageField(upload_to='images/items/',null=True)
    feedback_photo = models.ImageField(upload_to='images/items/',null=True)
    thumbnail = models.ImageField(upload_to='images/items/thumbnails',null=True)
    thumbnail1 = models.ImageField(upload_to='images/items/thumbnails',null=True)
    thumbnail2 = models.ImageField(upload_to='images/items/thumbnails',null=True)
    thumbnail3 = models.ImageField(upload_to='images/items/thumbnails',null=True)


