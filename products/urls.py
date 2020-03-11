from django.conf.urls import url, include
from .views import home_page

urlpatterns = [
    url(r'^$', home_page, name='products'),
]