from django.db import models


# Create your models here.
class Stock(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    stock_status = models.CharField(max_length=50)
    available_stock = models.PositiveIntegerField()
    date = models.DateField(default='1994-05-03')

    def __str__(self):
        return self.name
