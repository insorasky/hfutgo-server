from django.db import models


class Lesson(models.Model):
    sid = models.IntegerField(db_index=True)
    sname = models.TextField()
    name = models.CharField(max_length=100, db_index=True)
    code = models.CharField(max_length=20, db_index=True)
    credit = models.IntegerField(db_index=True)
    classcode = models.TextField()
    classname = models.CharField(max_length=80, db_index=True)
    type = models.CharField(max_length=30, db_index=True)
    department = models.CharField(max_length=50, db_index=True)
    teacher = models.CharField(max_length=50, db_index=True)
    info = models.JSONField()
    campus = models.CharField(max_length=15, db_index=True)
    lessons = models.IntegerField(db_index=True)
    weeks = models.IntegerField(db_index=True)
    weeklessons = models.IntegerField(db_index=True)
    personlimit = models.IntegerField(db_index=True)
