from django.conf.urls import url
from .views import checkout,checkout_bid

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^auction/$', checkout_bid, name='checkout_bid'),
]