from django.conf.urls import url
from .views import bid_view

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', bid_view, name="bid_view")
]