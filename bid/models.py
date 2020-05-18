from django.db import models
from django.contrib.auth.models import User
from products.models import Product

""" Product Bid model linked to Product model via Foreing Key """
class ProductBid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return self.product.name

""" Bid Model linked to Product Bid model via Foreing Key, stores the amount the user and the product """
class Bid(models.Model):
    product = models.ForeignKey(ProductBid,on_delete=models.CASCADE,blank=False,related_name="bids")
    bid = models.DecimalField(max_digits=10, decimal_places=3,null=True,default="",blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default="")

    
    def __str__(self):
        return "{0} | {1} | {2}".format(
            self.product, self.user, self.bid)