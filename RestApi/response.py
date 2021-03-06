#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Fri Aug 25 2017
# File: response.py
# 
# Description: 
#
from django.http import JsonResponse
from enum import Enum, unique

class ResponseStatus(Enum):
    OK = ("操作成功",0)
    SERIALIZER_ERROR = ("序列化失败",1)
    OBJECT_NOT_EXSIT = ("对象不存在",2)
    PUSH_FAILED = ("推送失败",3)
    PARAMS_ERROR = ("参数错误",4)
    UNSUPPORT_ACTION = ("不支持的操作",5)

class RestResponse(JsonResponse):
    
    """
    Rest Response Constact
    """
    def __init__(self, data, message=None, detail=None, errCode=0, status=ResponseStatus.OK):
        
        tips = status.value[0]
        code = status.value[1]
        
        response = {
            'code':code,
            'message':tips,
            'detail':detail,
            'data':data
        }
        super(RestResponse, self).__init__(response, status=200)

        ###允许跨域
        self["Access-Control-Allow-Origin"] = "*"
        self["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        self["Access-Control-Max-Age"] = "1000"
        self["Access-Control-Allow-Headers"] = "*"