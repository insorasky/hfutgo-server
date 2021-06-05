from django.db import models


class DakaUser(models.Model):
    user = models.CharField(max_length=10, db_index=True)
    openid = models.CharField(max_length=128)
    password = models.CharField(max_length=8)
    create_time = models.DateTimeField(auto_now_add=True)


class DakaLog(models.Model):
    user = models.CharField(max_length=10)
    status = models.IntegerField()
    log = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
