from django.db import models
from wxUser.models import UserInfo


class RoadBook(models.Model):
    route = models.TextField()
    chargers = models.CharField(max_length=2048)
    startPoint = models.CharField(max_length=256)
    destination = models.CharField(max_length=256)
    createUser = models.ForeignKey(UserInfo,
                                     to_field='username',
                                     on_delete=models.CASCADE,
                                     max_length=150)
    createTime = models.TimeField(auto_now_add=True)
    collectedCount = models.IntegerField(default=0)
