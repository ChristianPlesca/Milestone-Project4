from django.conf.urls import url
from .views import search, sort_by_max_price,sort_by_min_price


urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^$', sort_by_max_price, name='sort_by_max_price'),
    url(r'^$', sort_by_min_price, name='sort_by_min_price')
]