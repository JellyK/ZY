from django.shortcuts import render
from .models import ECharger, TeslaCharger
from django.http import JsonResponse
import json

def charger(request):
    chargerId = request.GET.get('id')
    chargerType = request.GET.get('type')
    j = dict()
    if chargerType == 'teslaCharger':
        try:
            teslaCharger = TeslaCharger.objects.get(location_id=chargerId)
        except teslaCharger.objects.model.DoesNotExist:
            return JsonResponse({'path': '/charger',
                                 'status': 'error',
                                 'reason': 'no this charger'})
        j['title'] = teslaCharger.title
        j['locationType'] = teslaCharger.location_type
        j['locationInfo'] = teslaCharger.street_address
        j['timeInfo'] = teslaCharger.opening_time_info
        j['chargerInfo'] = teslaCharger.charger_info
        j['chargeInfo'] = teslaCharger.charge_info
        j['telInfo'] = teslaCharger.tel_info
        j['latitude'] = teslaCharger.latitude
        j['longitude'] = teslaCharger.longitude
    elif chargerType == 'eCharger':
        pass

    return JsonResponse({
        'path': '/charger',
        'status': 'ok',
        'data': j
    })


def collect(request):
    return JsonResponse()


def teslaChargers(request):
    print('---------------------tesla')
    chargers = TeslaCharger.objects.all().values('location_id', 'latitude', 'longitude', 'title')
    jArray = makeJsonArray(chargers, 'location_id', 'latitude', 'longitude', 'title')
    print(jArray)
    return JsonResponse({
        'path': '/teslaChargers',
        'status': 'ok',
        'data': jArray
    })


def teslaSuperChargers(request):
    print('--------------------teslasuper')
    chargers = TeslaCharger.objects.all().values('location_id',
                                                 'location_type',
                                                 'latitude',
                                                 'longitude',
                                                 'title')
    jArray = makeTeslaJsonArray(chargers, 'supercharger')
    return JsonResponse({
        'path': '/teslaSuperChargers',
        'status': 'ok',
        'data': jArray
    })


def teslaDestinationChargers(request):
    print('--------------------tesladestination')
    chargers = TeslaCharger.objects.all().values('location_id',
                                                 'location_type',
                                                 'latitude',
                                                 'longitude',
                                                 'title')
    jArray = makeTeslaJsonArray(chargers, 'destination charger')
    return JsonResponse({
        'path': '/teslaDestinationChargers',
        'status': 'ok',
        'data': jArray
    })


def eChargers(request):
    print('--------------------e')
    chargers = ECharger.objects.all().values('chargerId', 'lat', 'lng', 'company')
    jArray = makeJsonArray(chargers, 'chargerId', 'lat', 'lng', 'company')
    return JsonResponse({
        'path': '/eChargers',
        'status': 'ok',
        'data': jArray
    })


def makeJsonArray(chargers, location_id, latitude, longitude, title):
    jArray = []
    for charger in chargers:
        jArray.append({
            # 'id': charger['id'],
            'location_id': charger[location_id],
            'latitude': charger[latitude],
            'longitude': charger[longitude],
            'title': charger[title]
        })
    return jArray


def makeTeslaJsonArray(chargers, chargerType):
    jArray = []
    for charger in chargers:
        if chargerType in charger['location_type']:
            jArray.append({
                # 'id': charger['id'],
                'location_id': charger['location_id'],
                'latitude': charger['latitude'],
                'longitude': charger['longitude'],
                'title': charger['title']
            })
    return jArray