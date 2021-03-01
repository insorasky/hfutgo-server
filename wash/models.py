from django.db import models


class Building(models.Model):
    name = models.TextField(default=None)
    sort = models.IntegerField(default=None)
    campus = models.TextField(default=None)

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.TextField(default=None)
    building = models.TextField(default=None)
    type = models.IntegerField(default=None)
    sort = models.IntegerField(default=None)
    NQT = models.TextField(default=None)
    machineid = models.TextField(default=None)

    def __str__(self):
        return self.name
