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
    avatarUrl = models.CharField(max_length=128, default='')
    nickName = models.CharField(max_length=64, default='')
    gender = models.SmallIntegerField(default=0)
    city = models.CharField(max_length=32, default='')
    province = models.CharField(max_length=32, default='')
    country = models.CharField(max_length=32, default='')
    car_type = models.CharField(max_length=64)
    '''
    road_book 记录了用户的所有完成，未完成和收藏的路书，以json格式
    {"id": roadBook_id, "completed": 1, "collected": 1, "commented": 1}作为数据，其中
    '''
    road_book = models.TextField(max_length=65536, default='[]')
    charger = models.TextField(max_length=65536, default='[]')
    comment = models.TextField(max_length=65536, default='[]')

    # class Meta:
    #     db_table = 'userinfo'
