#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Tue Aug 29 2017
# File: constant.py
# 
# Description: 
#


OK = 0                    #正常调用
ERR_MISS_PARAMS = 1       #缺少参数 
ERR_PARAMS_ERROR = 2      #参数错误
ERR_DEVICE_NOT_EXSIT = 3  #设备不存在
ERR_PUSH_MESSAGE_FAILED = 4  #推送出错
ERR_PARSE_JSON_FAILED = 5    #解析JSON出错
ERR_DEVICE_EMPTY = 6   #没有设备
ERR_USER_NOT_EXSIT = 9  #用户不存在
ERR_NEWS_NOT_EXSIT = 10

ERR_XINGE_BUSY = 7     #信鸽服务器繁忙
ERR_XINGE_TOEKN_NOT_EXSIT = 40  #不存在的device_token
ERR_XINGE_APNS_BUSY = 71 #APNS服务器繁忙
ERR_XINGE_MSG_TOO_LONG = 73  #消息数据太长(iOS长度限制:256个字节,Android长度限制:800个字节)
ERR_XINGE_MSG_FREQUENT =76 #请求太过频繁