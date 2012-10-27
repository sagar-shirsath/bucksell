from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import slugify
import random
import re
from django.db.models import Q
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
    def normalize_query(self,query_string,
                        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                        normspace=re.compile(r'\s{2,}').sub):
        ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
            and grouping quoted words together.
            Example:

            >>> normalize_query('  some random  words "with   quotes  " and   spaces')
            ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

        '''
        return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

    def get_query(self,query_string, search_fields):
        ''' Returns a query, that is a combination of Q objects. That combination
            aims to search keywords within a model by testing the given search fields.

        '''
        query = None # Query to search for every search term
        terms = self.normalize_query(query_string)
        for term in terms:
            or_query = None # Query to search for a given term in each field
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return query






class ItemPhoto(models.Model):
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



