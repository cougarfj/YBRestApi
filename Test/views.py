from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.request import QueryDict
from RestApi.response import RestResponse
from Push import xgpush
from Push.constant import *
from Push.models import Device
import json



@csrf_exempt
@api_view(['POST'])
def message_to_all(request):
    """
    推送消息到所有设备
    """
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')
    alert = data.get('alert')
    custom_data = data.get('custom_data')
    if alert == None:
        return RestResponse(data=None, message="参数缺失", detail="alert is required", errCode = ERR_MISS_PARAMS)
    if custom_data != None:
        try:
            custom_data = json.loads(custom_data)
        except:
            return RestResponse(data=None, message="参数类型错误", detail="custom_data can not be parse json", errCode = ERR_PARSE_JSON_FAILED)
    
    devices = Device.objects.all()
    if len(devices) == 0 :
       return RestResponse(data=None,message="没有绑定设备", errCode=ERR_DEVICE_EMPTY)
    else:
       device_list = []
       for device in devices:
           device_list.append(device.device_token)
    
    result = xgpush.push_message_to_multiple(device_token_list = device_list, message = alert, custom_data= custom_data)

    if result[0] == OK:
        return RestResponse(data=data, message="发送推送数据成功")
    else:
        return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])
        


@csrf_exempt
@api_view(['POST'])
def message_to_one(request):
    """
    推送消息到单个设备
    """

    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')
    device_token = data.get('device_token')
    alert = data.get('alert')
    custom_data = data.get('custom_data')
    if device_token == None:
        return RestResponse(data=None, message="参数缺失", detail="device_token is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="参数缺失", detail="alert is required", errCode = ERR_MISS_PARAMS)
    if custom_data != None:
        try:
            custom_data = json.loads(custom_data)
        except:
            return RestResponse(data=None, message="参数类型错误", detail="custom_data can not be parse json", errCode = ERR_PARSE_JSON_FAILED)

    try:
        device = Device.objects.get(device_token=device_token)
        result = (0,'')
        if device.is_ios():
            result = xgpush.push_ios_message(device_token = device_token, message = alert, custom_data = custom_data)
        if device.is_android():
            result = xgpush.push_android_message(device_token = device_token, title = '1234TV', message = alert, custom_data = custom_data)
        
        if result[0] == 0:
            return RestResponse(data=data, message="发送推送数据成功")
        else:
            return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])


    except Device.DoesNotExist:
        return RestResponse(data=None, message="不存在该设备", detail="device is not exist", errCode = ERR_DEVICE_NOT_EXSIT)

    

@csrf_exempt
@api_view(['POST'])
def message_to_multiple(request):
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')
    device_token_list = data.get('device_token_list')
    alert = data.get('alert')
    custom_data = data.get('custom_data')
    if device_token_list == None:
        return RestResponse(data=None, message="参数缺失", detail="device_token_list is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="参数缺失", detail="alert is required", errCode = ERR_MISS_PARAMS)
    if custom_data != None:
        try:
            custom_data = json.loads(custom_data)
        except:
            return RestResponse(data=None, message="参数类型错误", detail="custom_data can not be parse json", errCode = ERR_PARSE_JSON_FAILED)

    device_token_list = json.loads(device_token_list)
    result = xgpush.push_message_to_multiple(device_token_list = device_token_list, message = alert, custom_data = custom_data)

    if result[0] == OK:
        return RestResponse(data=data, message="发送推送数据成功")
    else:
        return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])