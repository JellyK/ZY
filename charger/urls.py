from django.urls import path
from . import views

urlpatterns = [
    path('charger', views.charger),
    path('collect', views.collect),
]