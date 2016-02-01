# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

from utils.validators import Phone
from ..models import Message


class UsrSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class MessageSerializer(serializers.ModelSerializer):

    # read only fields
    id = serializers.IntegerField(read_only=True)
    c_time = serializers.DateTimeField(read_only=True)
    u_time = serializers.DateTimeField(read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    # write & read fields
    phone = serializers.CharField(validators=[Phone()])
    msg = serializers.CharField()
    device = serializers.CharField()

    class Meta:
        model = Message
        fields = ('id', 'c_time', 'u_time', 'user', 'phone', 'msg', 'device')


