from django.db import models


class TeslaCharger(models.Model):
    location_id = models.CharField(max_length=64, unique=True, blank=False, default='')
    location_type = models.CharField(max_length=64, blank=False)
    open_soon = models.SmallIntegerField()
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    title = models.CharField(max_length=32)
    street_address = models.CharField(max_length=64)
    extended_address = models.CharField(max_length=64, default='')
    locality = models.CharField(max_length=16)
    tel_info = models.CharField(max_length=64)
    opening_time_info = models.CharField(max_length=256)
    charger_info = models.CharField(max_length=256)
    charge_info = models.CharField(max_length=256)

    # class Meta:
    #     db_table = 'teslacharger'


class ECharger(models.Model):
    address = models.CharField(max_length=128, blank=False)
    areaName = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    connectorType = models.SmallIntegerField()
    currentType = models.SmallIntegerField()
    freeNum = models.SmallIntegerField()
    chargerId = models.CharField(max_length=64, unique=True, blank=False, default='')
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

    # class Meta:
    #     db_table = 'echarger'
