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
