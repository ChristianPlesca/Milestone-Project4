from django.conf.urls import url, include
from .views import home_page,product_details

urlpatterns = [
    url(r'^$', home_page, name='index'),
    url(r'^(?P<pk>\d+)$', product_details, name='product_details'),

]