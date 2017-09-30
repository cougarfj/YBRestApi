#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Thu Aug 24 2017
# File: serializers.py.py
# 
# Description: 
#

from rest_framework import serializers
from Push.models import Device,PushMessage,OpenWebPushMessage


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = ('device_token', 'device_type', 'user_id', 'update_time', 'is_delete')



class PushMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PushMessage
        fields = ('push_id', 'alert', 'user_ids', 'custom_data')


class OpenWebPushMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenWebPushMessage
        field = ('push_id', 'alert', 'user_ids', 'custom_data')