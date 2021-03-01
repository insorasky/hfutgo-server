from django.db import models


class Lesson(models.Model):
    sid = models.TextField()
    sname = models.TextField()
    name = models.TextField()
    code = models.TextField()
    credit = models.TextField()
    classcode = models.TextField()
    classname = models.TextField()
    type = models.TextField()
    department = models.TextField()
    teacher = models.TextField()
    info = models.JSONField()
    campus = models.TextField()
    lessons = models.TextField()
    weeks = models.TextField()
    weeklessons = models.TextField()
    personlimit = models.TextField()
