from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'word_index'),
    url(r'^word$', views.word, name = 'word_word'),
    url(r'^reset$', views.reset, name = 'word_reset'),
]
