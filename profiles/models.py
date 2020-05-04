from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='', blank=True,null=True)
    city = models.CharField(max_length=100, default='', blank=True)
    website = models.URLField(default='', blank=True)
    phone = models.CharField(default="", max_length=50, blank=True,null=True)
    image = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username


