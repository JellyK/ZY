from django.shortcuts import render
from .models import ECharger

def charger(request):
    chargerId = request.GET.get('id')
    chargerType = request.GET.get('type')
    if chargerType == 'teslaCharger':
        pass
    elif chargerType == 'eCharger':
        pass
