from django.shortcuts import render
from .models import RoadBook
from wxUser.models import UserAccess, UserInfo
from django.http import JsonResponse
import json


def create(request):
    # print(request.method)
    # print(request.POST)
    route = json.loads(request.POST.get('route'))
    routePoints = json.loads(request.POST.get('routePoints'))
    chargers = routePoints['chargers']
    startPoint = routePoints['startPoint']
    destination = routePoints['destination']
    token = request.POST.get('token')

    try:
        user_access = UserAccess.objects.get(token=token)
        print('testtest:' + user_access.username)
    except UserAccess.objects.model.DoesNotExist:
        print('aaa')
        return JsonResponse({'path': '/user',
                             'status': 'error',
                             'reason': 'token is error'})

    # roadBook, is_created = RoadBook.objects.get_or_create(chargers=chargers,
    #                                                       startPoint=startPoint,
    #                                                       destination=destination)
    # if is_created:
    #     roadBook.route = route
    #     roadBook.createUser = user_access.username
    #     roadBook.save()
    #     ret += 'create a new roadBook successfully\n'
    # else:
    #     if roadBook.route != route:
    #         roadBook = RoadBook.objects.create(chargers=chargers,
    #                                               startPoint=startPoint,
    #                                               destination=destination,
    #                                               route=route,
    #                                               createUser=user_access.username)
    #         ret += 'create a new roadBook which has the same routePoints and different route\n'
    #     else:
    #         ret += 'has the same roadBook in database\n'


    try:
        user_info = UserInfo.objects.get(username=user_access.username)
        print('testtest:' + user_access.username)
    except UserInfo.objects.model.DoesNotExist:
        print('bbb')
        return JsonResponse({'path': '/user',
                             'status': 'error',
                             'reason': 'userInfo is not found'})

    roadBook = RoadBook.objects.create(chargers=chargers,
                                       startPoint=startPoint,
                                       destination=destination,
                                       route=route,
                                       createUser=user_info)

    print('userInfo.RoadBook:', user_info.road_book)
    roadBooks = json.loads(user_info.road_book)
    roadBooks.append({
        "id": roadBook.id,
        "completed": 0,
        "collected": 0,
        "commented": 0
    })
    user_info.road_book = json.dumps(roadBooks)
    user_info.save()

    return JsonResponse({
        'path': '/update',
        'status': 'ok',
        'data': {
            "id": roadBook.id,
            "completed": 0,
            "collected": 0,
            "commented": 0
        }
    })