from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'ninja_index'),
    url(r'^ninjas$', views.ninjas, name = 'ninja_ninjas'),
    url(r'^(?P<color>\w+)$', views.one_ninja, name = 'ninja_oneninja')

]
