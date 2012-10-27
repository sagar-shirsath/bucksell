from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    subject = models.CharField(max_length=50)
    to_user = models.ForeignKey(User , related_name='to_user')
    from_user = models.ForeignKey(User , related_name='from_user')
    body = models.TextField()
    read = models.BooleanField(default=False)
