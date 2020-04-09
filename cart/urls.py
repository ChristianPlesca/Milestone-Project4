from django.conf.urls import url, include
from .views import cart,add_to_cart


urlpatterns = [
    url(r'^$', cart, name='cart'),
    url(r'^add-to-cart/(?P<id>\d+)', add_to_cart, name='add-to-cart')
]
