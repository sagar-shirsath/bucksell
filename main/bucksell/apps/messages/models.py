from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message():
    subject = models.CharField(max_length=50)
    to_user = models.ForeignKey(User , related_name='to')
    from_user = models.ForeignKey(User , related_name='from')
    body = models.TextField()
    read = models.BooleanField(default=False)
