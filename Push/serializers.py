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
from Push.models import Device
from Push.constant import *

class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = ('device_token', 'device_type', 'user_id', 'update_time', 'is_delete')



class PushMessageSerializer(serializers.Serializer):

    alert = serializers.CharField(max_length=200)
    user_ids = serializers.CharField(max_length=21800)
    custom_data = serializers.CharField(max_length=21800, required=False)

    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance, data, **kwargs)
        self.alert = data.get('alert')
        self.user_ids = data.get('user_ids')

class OpenWebPushMessageSerializer(PushMessageSerializer):
    
    url = serializers.CharField(max_length=200) 

    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.url = data.get('url')
        self.custom_data = {"action":PUSH_ACTION_OPEN_WEBVIEW,"data":{"url":self.url}}


class OpenLiveRoomPushMessageSerializer(PushMessageSerializer):
    room_id = serializers.CharField(max_length=200) 
    eng_name = serializers.CharField(max_length=200)
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.room_id = data.get('room_id')
        self.eng_name = data.get('eng_name')
        self.custom_data = {"action":PUSH_ACTION_OPEN_LIVEROOM,"data":{"room_id":self.room_id,"eng_name":self.eng_name}}

class OpenTeamHallMessageSerializer(PushMessageSerializer):
    eng_name = serializers.CharField(max_length=200)
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.eng_name = data.get('eng_name')
        self.custom_data = {"action":PUSH_ACTION_OPEN_TEAMHALL,"data":{"eng_name":self.eng_name}}