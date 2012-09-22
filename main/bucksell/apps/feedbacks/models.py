from django.db import models
from django.contrib.auth.models import User
from items.model import Item
# Create your models here.

class Feedback():
    subject = models.CharField(max_length=50)
    to_user = models.ForeignKey(User , related_name='to')
    from_user = models.ForeignKey(User , related_name='from')
    body = models.TextField()
    item = models.ForeignKey(Item)
    is_public = models.BooleanField(default=False)
