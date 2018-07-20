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
    car_type = models.CharField(max_length=1024)
    road_book = models.CharField(max_length=1024)
    charger = models.CharField(max_length=1024)

    # class Meta:
    #     db_table = 'userinfo'
