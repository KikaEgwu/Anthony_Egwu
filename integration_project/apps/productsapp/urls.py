from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'product_index'),
    url(r'^create$', views.product_create, name = 'product_create'),
    url(r'^(?P<id>\d+)$', views.product_show, name = 'product_show'),
    url(r'^(?P<id>\d+)/edit$', views.product_edit, name = 'product_edit'),
    url(r'^(?P<id>\d+)/update$', views.product_update, name = 'product_update'),
    url(r'^(?P<id>\d+)/delete$', views.product_delete, name = 'product_delete'),
    url(r'^reviews/create$',  views.review_create, name = 'review_create'),

]
