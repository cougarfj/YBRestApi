#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Mon Aug 28 2017
# File: xgpush.py
# 
# Description: 
#

from xinge_push import xinge,constant,style

ANDROID_ACCESS_ID = 2100264608
ANDROID_SECRET_KEY = "ed039c53e8beccdf7ff6a536c9dc9e5d"


IOS_ACCESS_ID = 2200264610
IOS_SECRET_KEY = "273ba87ddee33ac14a865535e3f97f97"



android_push = xinge.XingeApp(accessId = ANDROID_ACCESS_ID, secretKey = ANDROID_SECRET_KEY)
ios_push = xinge.XingeApp(accessId = IOS_ACCESS_ID, secretKey = IOS_SECRET_KEY)

def push_ios_message(device_token, message, custom_data = {}):
    msg = xinge.MessageIOS()
    msg.alert = message
    msg.expireTime = 300
    msg.custom = {}
    msg.badge = 1
    msg.sound = "default"
    return ios_push.PushSingleDevice(deviceToken = device_token, message = msg, environment = constant.ENV_DEV)



def push_android_message(device_token, title, message, custom_data = {}):
    msg = xinge.Message()
    msg.type = constant.MESSAGE_TYPE_ANDROID_NOTIFICATION
    msg.title = title
    msg.content = message
    msg.expireTime = 300
    msg.custom = {}
    msg.style = style.Style()

    return android_push.PushSingleDevice(deviceToken = device_token, message = msg)