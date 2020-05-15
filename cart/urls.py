from django.conf.urls import url, include
from .views import view_cart,add_to_cart,delete_from_cart,add_to_cart_bid,view_cart_bid,delete_from_cart_bid


urlpatterns = [
    url(r'^$', view_cart, name='cart'),
    url(r'^bid/$', view_cart_bid, name='view_cart_bid'),
    url(r'^add-to-cart/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^add-to-cart-bid/(?P<id>\d+)', add_to_cart_bid, name='add_to_cart_bid'),
    url(r'^delete_from_cart/(?P<id>\d+)', delete_from_cart, name='delete_from_cart'),
    url(r'^delete_from_cart_bid/(?P<id>\d+)', delete_from_cart_bid, name='delete_from_cart_bid')
]
