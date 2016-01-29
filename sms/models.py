# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='messages')
    msg = models.CharField(max_length=140)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)
    device = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, default='')
    status = models.SmallIntegerField(default=0)
