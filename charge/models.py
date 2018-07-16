from django.db import models
import json

class TeslaCharge(models.Model):
    pass

class ECharge(models.Model):
    address = models.CharField(max_length=128, blank=False)
    areaName = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    connectorType = models.SmallIntegerField()
    currentType = models.SmallIntegerField()
    freeNum = models.SmallIntegerField()
    chargeId = models.CharField(max_length=64, unique=True, blank=False, default='')
    images = models.CharField(max_length=128, null=True)
    isGs = models.SmallIntegerField()
    lat = models.FloatField(blank=False)
    link = models.SmallIntegerField()
    lng = models.FloatField(blank=False)
    mapIcon = models.CharField(max_length=128)
    maxOutPower = models.SmallIntegerField()
    operatorTypes = models.CharField(max_length=32)
    payType = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    plugType = models.SmallIntegerField()
    priceRational = models.IntegerField()
    province = models.CharField(max_length=32)
    quantity = models.SmallIntegerField()
    score = models.SmallIntegerField()
    serviceCode = models.SmallIntegerField()
    standard = models.SmallIntegerField()
    status = models.SmallIntegerField()
    supportOrder = models.SmallIntegerField()