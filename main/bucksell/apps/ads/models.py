from django.db import models

# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    photo = models.ImageField(upload_to='images/photo')
    is_published = models.BooleanField(default=False)