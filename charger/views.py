from django.shortcuts import render
from .models import ECharger, EChargerInfo, TeslaCharger
from django.http import JsonResponse
import json

def charger(request):
    chargerId = request.GET.get('id')
    chargerType = request.GET.get('type')
    j = dict()
    if chargerType.startswith('tesla') and chargerType.endswith('Charger'):
        try:
            teslaCharger = TeslaCharger.objects.get(location_id=chargerId)
        except TeslaCharger.objects.model.DoesNotExist:
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
        try:
            eCharger = ECharger.objects.get(chargerId=chargerId)
            eChargerInfo = EChargerInfo.objects.get(chargerId=chargerId)
        except EChargerInfo.objects.model.DoesNotExist:
            return JsonResponse({'path': '/charger',
                                 'status': 'error',
                                 'reason': 'no this charger'})
        except EChargerInfo.objects.model.DoesNotExist:
            return JsonResponse({'path': '/charger',
                                 'status': 'error',
                                 'reason': 'no this charger'})
        j['name'] = eChargerInfo.name
        j['latitude'] = eCharger.lat
        j['longitude'] = eCharger.lng
        j['operator'] = eChargerInfo.operatorName
        j['acNum'] = json.loads(eChargerInfo.chargerTypeNum.replace('\'', '\"'))['1']
        j['dcNum'] = json.loads(eChargerInfo.chargerTypeNum.replace('\'', '\"'))['2']
        j['businessTime'] = eChargerInfo.businessTime
        j['electricizePrice'] = eChargerInfo.electricizePrice
        j['parkingPrice'] = eChargerInfo.priceParking

    return JsonResponse({
        'path': '/charger',
        'status': 'ok',
        'data': j
    })


def collect(request):
    return JsonResponse()


def teslaChargers(request):
    print('---------------------tesla')
    chargers = TeslaCharger.objects.all().values('location_id',
                                                 'latitude',
                                                 'longitude',
                                                 'title',
                                                 'open_soon')
    jArray = makeJsonArray(chargers, 'location_id', 'latitude', 'longitude', 'title', judge='open_soon')
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
                                                 'title',
                                                 'open_soon')
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
                                                 'title',
                                                 'open_soon')
    jArray = makeTeslaJsonArray(chargers, 'destination charger')
    return JsonResponse({
        'path': '/teslaDestinationChargers',
        'status': 'ok',
        'data': jArray
    })


def eChargers(request):
    print('--------------------e')
    chargers = ECharger.objects.all().values('chargerId', 'lat', 'lng', 'company', 'isGs')
    jArray = makeJsonArray(chargers, 'chargerId', 'lat', 'lng', 'company', judge='isGs')
    return JsonResponse({
        'path': '/eChargers',
        'status': 'ok',
        'data': jArray
    })


def makeJsonArray(chargers, location_id, latitude, longitude, title, judge=None):
    jArray = []
    for charger in chargers:
        j = {
            # 'id': charger['id'],
            'location_id': charger[location_id],
            'latitude': charger[latitude],
            'longitude': charger[longitude],
            'title': charger[title]
        }
        if judge != None:
            if judge == 'isGs' and charger[judge] == 0:
                continue
            elif judge == 'open_soon' and charger[judge] == 1:
                continue
        jArray.append(j)
    return jArray


def makeTeslaJsonArray(chargers, chargerType):
    jArray = []
    for charger in chargers:
        if chargerType in charger['location_type'] and charger['open_soon'] == 0:
            jArray.append({
                # 'id': charger['id'],
                'location_id': charger['location_id'],
                'latitude': charger['latitude'],
                'longitude': charger['longitude'],
                'title': charger['title']
            })
    return jArray