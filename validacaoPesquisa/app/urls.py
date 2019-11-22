from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'^carro_new/', carro_new, name='carro_new'),
    url(r'^carro_list/', carro_list, name='carro_list'),
    url(r'^carro_edit/(?P<pk>[0-9]+)', carro_edit, name='carro_edit'),
    url(r'^carro_delete/(?P<pk>[0-9]+)', carro_delete, name='carro_delete'),
]