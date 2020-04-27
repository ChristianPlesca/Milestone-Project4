from django.db import models
from django.contrib.auth.models import User

class Bid(models.Model):
    bid = models.DecimalField(max_digits=10, decimal_places=3,blank=False)
    user = models.OneToOneField(User)
