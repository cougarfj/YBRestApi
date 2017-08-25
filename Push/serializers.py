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


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = ('device_token', 'device_type', 'user_id')