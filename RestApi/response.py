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

class RestResponse(JsonResponse):
    """
    Rest Response Constact
    """
    def __init__(self, data, message, detail=None, errCode=0):
        response = {
            'code':errCode,
            'message':message,
            'detail':detail,
            'data':data
        }
        super(RestResponse, self).__init__(response, status=200)
