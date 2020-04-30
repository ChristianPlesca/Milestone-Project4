from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserBid(models.Model):
    user_bid = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default="")
    
    def __str__(self):
        return self.user_bid.username


class Bid(models.Model):
    user = models.ForeignKey(UserBid,on_delete=models.CASCADE,blank=False,default="")
    bid = models.DecimalField(max_digits=10, decimal_places=3,null=True,default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True,default="")
    
    def __str__(self):
        return "{0} | {1} | {2}".format(
            self.user, self.product.name, self.bid)