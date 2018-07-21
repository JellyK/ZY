from django.shortcuts import render
from .models import ECharger, TeslaCharger
from django.http import JsonResponse
import json

def charger(request):
    chargerId = request.GET.get('id')
    chargerType = request.GET.get('type')
    if chargerType == 'teslaCharger':
        try:
            teslaCharger = TeslaCharger.objects.get(location_id=chargerId)
        except teslaCharger.objects.model.DoesNotExist:
            return JsonResponse({'path': '/charger',
                                 'status': 'error',
                                 'reason': 'no this charger'})
        j = dict()
        j['title'] = teslaCharger.title
        j['chargerType'] = 'teslaCharger'
        j['locationInfo'] = teslaCharger.street_address
        j['timeInfo'] = teslaCharger.opening_time_info
        j['chargerInfo'] = teslaCharger.charger_info
        j['chargeInfo'] = teslaCharger.charge_info
        j['telInfo'] = teslaCharger.tel_info
    elif chargerType == 'eCharger':
        pass

    return JsonResponse({
        'path': '/charger',
        'status': 'ok',
        'data': j
    })

def collect(request):
    return JsonResponse()