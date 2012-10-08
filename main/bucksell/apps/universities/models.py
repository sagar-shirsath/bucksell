from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/universities')
    address = models.TextField()
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    class Meta:
        verbose_name = 'University Management'
    def __unicode__(self):
        return self.name

