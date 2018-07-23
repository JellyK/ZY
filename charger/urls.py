from django.urls import path
from . import views

urlpatterns = [
    path('charger', views.charger),
    path('collect', views.collect),
    path('teslaChargers', views.teslaChargers),
    path('eChargers', views.eChargers),
    path('teslaSuperChargers', views.teslaSuperChargers),
    path('teslaDestinationChargers', views.teslaDestinationChargers)
]
