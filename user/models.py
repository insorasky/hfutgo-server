from django.db import models


class User(models.Model):
    name = models.TextField()
    student_id = models.CharField(max_length=10, db_index=True)
    organization = models.TextField()
    card_id = models.CharField(max_length=7, db_index=True, null=True)
    eduadmin_id = models.CharField(max_length=10, db_index=True, null=True)
    type = models.IntegerField()
    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


class LoginState(models.Model):
    type = models.IntegerField(db_index=True)  # 正常学生：1，游客：2，封网临时用户：3
    user_id = models.IntegerField()
    student_id = models.IntegerField(null=True)
    openid = models.CharField(max_length=64, null=True)
    token = models.UUIDField(db_index=True)
    vpn_ticket = models.TextField()
    at_token = models.TextField()
    available = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    destroy_time = models.DateTimeField(auto_now=True)


class Guest(models.Model):
    openid = models.CharField(max_length=64)
    unionid = models.CharField(max_length=64)
    nick_name = models.TextField()
    city = models.TextField()
    avatar = models.TextField()
