from django.db import models
from items.model import Item

# Create your models here.
class PaymentType(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField()
    transaction_charge = models.FloatField()
    key = models.CharField(max_length=50)

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    item = models.ForeignKey(Item)
    seller = models.ForeignKey(User , related_name='seller')
    buyer = models.ForeignKey(User , related_name='buyer')
    gross_amount = models.FloatField()
    discount = models.PositiveIntegerField(max_length=2)
    discount_revenue = models.FloatField()
    net_revenue = models.FloatField()
    texes = models.FloatField()
    transaction_charge = models.FloatField()
    payment_type = models.ForeignKey(PaymentType)
