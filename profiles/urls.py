from .views import profile
from django.conf.urls import url
from .views import edit_profile
urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^edit/(?P<pk>\d+)$', edit_profile, name='edit_profile'),
]