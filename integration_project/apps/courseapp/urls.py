from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'course_index'),
    url(r'^create', views.create, name = 'course_create'),
    url(r'^(?P<id>\d+)/delete', views.delete, name = 'course_delete'),
]
