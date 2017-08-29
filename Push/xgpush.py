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
from Push.constant import *


ANDROID_ACCESS_ID = 2100264608
ANDROID_SECRET_KEY = "ed039c53e8beccdf7ff6a536c9dc9e5d"


IOS_ACCESS_ID = 2200264610
IOS_SECRET_KEY = "273ba87ddee33ac14a865535e3f97f97"



android_push = xinge.XingeApp(accessId = ANDROID_ACCESS_ID, secretKey = ANDROID_SECRET_KEY)
ios_push = xinge.XingeApp(accessId = IOS_ACCESS_ID, secretKey = IOS_SECRET_KEY)

def push_ios_message(device_token, message, custom_data = {}):
    msg = buildIOSMessage(message = message, custom_data = custom_data)
    return ios_push.PushSingleDevice(deviceToken = device_token, message = msg, environment = constant.ENV_DEV)

def push_android_message(device_token, title, message, custom_data = {}):
    msg = buildAndroidMessage(message = message, custom_data = custom_data)
    return android_push.PushSingleDevice(deviceToken = device_token, message = msg)


def push_message_to_all(message, custom_data = {}):
    android_msg = buildAndroidMessage(message = message, custom_data = custom_data)
    ios_msg = buildIOSMessage(message=message, custom_data = custom_data)

    (errRet_Android,errMsg_Android) =  android_push.PushAllDevices(deviceType = 0, message = android_msg)
    (errRet_iOS,errMsg_iOS) = ios_push.PushAllDevices(deviceType = 0, message = ios_msg, environment = constant.ENV_DEV)
    
    if errRet_Android == 0 and errRet_iOS == 0 :
        return (constant.ERR_OK,None)
    elif errRet_Android != 0 and errRet_iOS == 0:
        return (errRet_Android,errMsg_Android)
    else:   
        return (errRet_iOS,errMsg_iOS)


def push_message_to_multiple(device_token_list, message, custom_data={}):
    android_msg = buildAndroidMessage(message = message, custom_data = custom_data)
    ios_msg = buildIOSMessage(message=message, custom_data = custom_data)

    result_android = android_push.CreateMultipush(android_msg)
    result_ios = ios_push.CreateMultipush(ios_msg,environment=constant.ENV_DEV)

    (errRet_Android,errMsg_Android) =  android_push.PushDeviceListMultiple(pushId = result_android[2], deviceList = device_token_list)
    (errRet_iOS,errMsg_iOS) = ios_push.PushDeviceListMultiple(pushId = result_ios[2], deviceList = device_token_list)

    if errRet_Android == 0 and errRet_iOS == 0 :
        return (constant.ERR_OK,None)
    elif errRet_Android != 0 and errRet_iOS == 0:
        return (errRet_Android,errMsg_Android)
    else:   
        return (errRet_iOS,errMsg_iOS)


def buildAndroidMessage(message,custom_data={}):
    msg = xinge.Message()
    msg.title = "1234TV"
    msg.content = message
    msg.type = constant.MESSAGE_TYPE_ANDROID_NOTIFICATION
    msg.expireTime = 86400
    if custom_data == None:
        msg.custom = {}
    else:
        msg.custom = custom_data

    msg.style = style.Style()
    return msg

def buildIOSMessage(message,custom_data={}):
    msg = xinge.MessageIOS()
    msg.alert = message
    msg.expireTime = 86400
    if custom_data == None:
        msg.custom = {}
    else:
        msg.custom = custom_data
    msg.badge = 1
    msg.sound = "default"
    return msg