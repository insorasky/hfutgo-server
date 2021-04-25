from django.db import models


class User(models.Model):
    name = models.TextField()
    student_id = models.CharField(max_length=10, db_index=True)
    organization = models.TextField()
    vpn_ticket = models.TextField()
    at_token = models.TextField()
    user_token = models.UUIDField(db_index=True)
    card_id = models.CharField(max_length=7, db_index=True)
    type = models.IntegerField()
    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
