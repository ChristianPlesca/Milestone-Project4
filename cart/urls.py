from django.conf.urls import url, include
from .views import view_cart,add_to_cart,delete_from_cart


urlpatterns = [
    url(r'^$', view_cart, name='cart'),
    url(r'^add-to-cart/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^delete_from_cart/(?P<id>\d+)', delete_from_cart, name='delete_from_cart')
]
