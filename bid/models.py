from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class ProductBid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, default="")
    def __str__(self):
        return self.product.name

class Bid(models.Model):
    product = models.ForeignKey(ProductBid,on_delete=models.CASCADE,blank=False,default="",related_name="bids")
    bid = models.DecimalField(max_digits=10, decimal_places=3,null=True,default="",blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default="")

    
    def __str__(self):
        return "{0} | {1} | {2}".format(
            self.product, self.user, self.bid)