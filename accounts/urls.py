from django.conf.urls import url, include
from . import urls_reset
from .views import register, logout, login

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]