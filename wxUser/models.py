from django.db import models


class UserAccess(models.Model):
    username = models.CharField(max_length=150, unique=True, blank=False)
    session_key = models.CharField(max_length=32)
    token = models.CharField(max_length=512)
    token_time = models.TimeField(auto_now=True)

    # class Meta:
    #     db_table = 'useraccess'


class UserInfo(models.Model):
    username = models.CharField(max_length=150, unique=True, blank=False)
    avatorUrl = models.CharField(max_length=128)
    nickName = models.CharField(max_length=64)
    gender = models.SmallIntegerField()
    city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    car_type = models.CharField(max_length=64)
    road_book = models.CharField(max_length=1024)
    charger = models.CharField(max_length=1024)
    comment = models.CharField(max_length=1024)

    # class Meta:
    #     db_table = 'userinfo'
