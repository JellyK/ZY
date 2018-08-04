from django.shortcuts import render
from .models import RoadBook
from django.http import JsonResponse
import json


def update(request):
    print(request.method)
    print(request.POST)
    return JsonResponse({
        'path': '/update',
        'status': 'ok',
        'data': {}
    })