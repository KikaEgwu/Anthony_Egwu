from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register', views.register, name = 'register'),
    url(r'^logon', views.logon, name = 'logon'),
    url(r'^dashboard', views.dashboard, name = 'dashboard'),
    url(r'^addbook$', views.addbook, name = 'addbook'),
    url(r'^addingbook$', views.addingbook, name = 'addingbook'),
    url(r'^logout', views.logout, name = 'logout'),
    url(r'^addreview$', views.addreview, name = 'addreview'),
]
