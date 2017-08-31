from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser
from rest_framework.renderers import JSONRenderer
from Push.serializers import DeviceSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.request import QueryDict
from RestApi.response import RestResponse
from Push.models import Device
from Push.constant import *
from Push import xgpush
import json


@csrf_exempt
@api_view(['POST'])
def live(request):
    """
    打开直播间页面
    """
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')

    room_id = data.get('room_id')
    eng_name = data.get('eng_name')
    alert = data.get('alert')

    if room_id == None:
        return RestResponse(data=None, message="room_id is required", errCode = ERR_MISS_PARAMS)
    if eng_name == None:
        return RestResponse(data=None, message="eng_name is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="alert is required", errCode = ERR_MISS_PARAMS)
    
    devices = Device.objects.all()
    custom_data = {"action":2,"data":{"room_id":room_id,"eng_name":eng_name}}
    device_list = []
    for device in devices:
        device_list.append(device.device_token)

    result = xgpush.push_message_to_multiple(device_token_list = device_list, message = alert, custom_data = custom_data)

    if result[0] == OK:
        return RestResponse(data=data, message="发送推送数据成功")
    else:
        return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])

@csrf_exempt
@api_view(['POST'])
def web(request):

    """
    通知打开web页面
    """
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')

    url = data.get('url')
    alert = data.get('alert')

    if url == None:
        return RestResponse(data=None, message="url is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="alert is required", errCode = ERR_MISS_PARAMS)

    devices = Device.objects.all()
    custom_data = {"action":1,"data":{"url":url}}
    device_list = []
    for device in devices:
        device_list.append(device.device_token)
        
    result = xgpush.push_message_to_multiple(device_token_list = device_list, message = alert, custom_data = custom_data)

    if result[0] == OK:
        return RestResponse(data=data, message="发送推送数据成功")
    else:
        return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])



@csrf_exempt
@api_view(['POST'])
def team(request):
    """
    打开团队首页
    """
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')

    eng_name = data.get('eng_name')
    alert = data.get('alert')

    if eng_name == None:
        return RestResponse(data=None, message="eng_name is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="alert is required", errCode = ERR_MISS_PARAMS)
    
    devices = Device.objects.all()
    custom_data = {"action":3,"data":{"eng_name":eng_name}}
    device_list = []
    for device in devices:
        device_list.append(device.device_token)
        
    result = xgpush.push_message_to_multiple(device_token_list = device_list, message = alert, custom_data = custom_data)

    if result[0] == OK:
        return RestResponse(data=data, message="发送推送数据成功")
    else:
        return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])