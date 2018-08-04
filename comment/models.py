from django.db import models
from wxUser.models import UserInfo


class Comment:
    username = models.ForeignKey(UserInfo,
                                     to_field='username',
                                     on_delete=models.CASCADE,
                                     max_length=150)
    type = models.CharField(max_length=16)
    objId = models.CharField(max_length=32)
    stars = models.SmallIntegerField()
    content = models.CharField(max_length=512)
    createTime = models.TimeField(auto_now_add=True)