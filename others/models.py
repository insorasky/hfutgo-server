from django.db import models


class Config(models.Model):
    name = models.TextField()
    value = models.JSONField()
    time = models.DateTimeField(auto_now_add=True)


class Notice(models.Model):
    text = models.TextField()
    show = models.BooleanField()
    page = models.TextField()
    theme = models.TextField()
    time = models.DateTimeField(auto_now=True)


class Log(models.Model):
    user = models.CharField(max_length=10)
    path = models.TextField()
    params = models.TextField()
    data = models.JSONField(default=dict)
    time = models.DateTimeField(auto_now=True)
