from django.db import models
from django.contrib.auth.models import User
from items.models import Item
# Create your models here.

class Feedback(models.Model):
    subject = models.CharField(max_length=50)
    to_user = models.ForeignKey(User , related_name='to')
    from_user = models.ForeignKey(User , related_name='from')
    body = models.TextField()
    item = models.ForeignKey(Item)
    is_public = models.BooleanField(default=False)
