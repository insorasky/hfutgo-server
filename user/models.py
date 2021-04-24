from django.db import models


class User(models.Model):
    name = models.TextField()
    student_id = models.CharField(max_length=10)
    class_name = models.TextField()
    vpn_ticket = models.TextField()
    at_token = models.TextField()
    type = models.IntegerField()
    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
