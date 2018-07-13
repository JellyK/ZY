from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('user', views.user),
]