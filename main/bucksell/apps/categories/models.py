from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    class Meta:
        verbose_name = 'Category'
