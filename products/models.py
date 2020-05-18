from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


""" Product Pictures model which is connected to the Product model via
    Foreing key allows you to attach multiple images to the Product Model """
class ProductsPictures(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    product_id = models.ForeignKey('Product', related_name='images')

    def __str__(self):
        return self.product_id.name  

""" The Product Model which allows you to insert product details """
class Product(models.Model):
    name = models.CharField(max_length=254, default="" , unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    bid_price = models.DecimalField(max_digits=10, decimal_places=3)
    author = models.CharField(max_length=254, default="")
    date_made = models.CharField(max_length=254, default="")
    country_made_in = models.CharField(max_length=254, default="")
    height = models.DecimalField(max_digits=5, decimal_places=1,null = True , blank=True)
    width = models.DecimalField(max_digits=5, decimal_places=1,null = True, blank=True)
    past_owners = models.TextField()
    views = models.IntegerField(default=0)
    sold = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=None)
    main_image = models.ImageField(upload_to='images/%Y/%m/%d')
    
    def __str__(self):
        return self.name
