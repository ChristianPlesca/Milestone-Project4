from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    initial_price = models.DecimalField(max_digits=6, decimal_places=2)
    bid_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.name