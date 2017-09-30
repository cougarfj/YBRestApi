from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser
from rest_framework.renderers import JSONRenderer
from Push.serializers import DeviceSerializer,OpenWebPushMessageSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.request import QueryDict
from RestApi.response import RestResponse,ResponseStatus
from Push.models import Device
from Push.constant import *
from Push import xgpush
import json
from rest_framework.decorators import parser_classes
from rest_framework import generics


class DeviceListView(generics.GenericAPIView):
    """
    查询列表
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        return RestResponse(data=serializer.data,status=ResponseStatus.OK)



class RegisterDeviceView(generics.GenericAPIView):
    
    """
    注册设备
    """

    serializer_class = DeviceSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        device_token = data.get('device_token')
        serializer = None
        try:
            device = Device.objects.get(device_token=device_token)
            serializer = self.get_serializer(device,data=data)
        except Device.DoesNotExist:
            serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return RestResponse(data=data,status=ResponseStatus.OK)
        else:
            return RestResponse(data=data,status=ResponseStatus.SERIALIZER_ERROR,detail=serializer.errors)



class UnRegisterDeviceView(generics.GenericAPIView):
    """
    解绑设备
    """
    serializer_class = DeviceSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        device_token = data.get('device_token')
        try:
            device = Device.objects.get(device_token=device_token)
            device.is_delete = True
            device.save()
            return RestResponse(data=data, status=ResponseStatus.OK)
        except Device.DoesNotExist:
            return RestResponse(data=data, status=ResponseStatus.OBJECT_NOT_EXSIT)



class NotifyOpenWebView(generics.GenericAPIView):
    """
    通知设备打开指定网页
    """
    serializer_class = OpenWebPushMessageSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            try:
                device_list = get_device_list(serializer.data.user_ids)
                result = xgpush.push_message_to_multiple(device_token_list = device_list, message = serializer.data.alert, custom_data = serializer.data.custom_data)
                if result[0] == OK:
                    return RestResponse(data=data, status=ResponseStatus.OK)
                else:
                    return RestResponse(data=data, status=ResponseStatus.PUSH_FAILED, detail=result[1])

            except Exception as e:
                return RestResponse(data=data,status=ResponseStatus.SERIALIZER_ERROR,detail=str(e))

        else:
            return RestResponse(data=data,status=ResponseStatus.SERIALIZER_ERROR,detail=serializer.errors)

        

        




def get_device_list(user_ids):
    user_id_list = json.loads(user_ids)
    device_list = []
    for user_id in user_id_list:
        devices = Device.objects.filter(user_id=user_id)
        for device in devices:
            device_list.append(device.device_token) 
    return device_list

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
    user_id = data.get('user_id')
    alert = data.get('alert')
    custom_data = data.get('custom_data')
    if user_id == None:
        return RestResponse(data=None, message="参数缺失", detail="user_id is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="参数缺失", detail="alert is required", errCode = ERR_MISS_PARAMS)
    if custom_data != None:
        try:
            custom_data = json.loads(custom_data)
        except:
            return RestResponse(data=None, message="参数类型错误", detail="custom_data can not be parse json", errCode = ERR_PARSE_JSON_FAILED)
    
    try:
        device = Device.objects.get(user_id=user_id)
        result = (0,'')
        if device.is_ios():
            result = xgpush.push_ios_message(device_token = device.device_token, message = alert, custom_data = custom_data)
        if device.is_android():
            result = xgpush.push_android_message(device_token = device.device_token, title = '1234TV', message = alert, custom_data = custom_data)
        
        if result[0] == 0:
            return RestResponse(data=data, message="发送推送数据成功")
        else:
            return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])


    except Device.DoesNotExist:
        return RestResponse(data=None, message="不存在该用户", detail="user_id is not exist", errCode = ERR_USER_NOT_EXSIT)
    except Device.MultipleObjectsReturned:
        device_list = []
        devices = Device.objects.filter(user_id=user_id)
        for device in devices:
            device_list.append(device.device_token)
        result = xgpush.push_message_to_multiple(device_token_list = device_list, message = alert, custom_data = custom_data)

        if result[0] == OK:
            return RestResponse(data=data, message="发送推送数据成功")
        else:
            return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])


@csrf_exempt
@api_view(['POST'])
def message_to_multiple(request):
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')
    user_id_list = data.get('user_id_list')
    alert = data.get('alert')
    custom_data = data.get('custom_data')
    if user_id_list == None:
        return RestResponse(data=None, message="参数缺失", detail="device_token_list is required", errCode = ERR_MISS_PARAMS)
    if alert == None:
        return RestResponse(data=None, message="参数缺失", detail="alert is required", errCode = ERR_MISS_PARAMS)
    if custom_data != None:
        try:
            custom_data = json.loads(custom_data)
        except:
            return RestResponse(data=None, message="参数类型错误", detail="custom_data can not be parse json", errCode = ERR_PARSE_JSON_FAILED)

    try:
        user_id_list = json.loads(user_id_list)
    except:
        return RestResponse(data=None, message="参数类型错误", detail="user_id_list can not be parse json", errCode = ERR_PARSE_JSON_FAILED)


    device_list = []
    for user_id in user_id_list:
        devices = Device.objects.filter(user_id=user_id)
        for device in devices:
            device_list.append(device.device_token)

    result = xgpush.push_message_to_multiple(device_token_list = device_list, message = alert, custom_data = custom_data)

    if result[0] == OK:
        return RestResponse(data=data, message="发送推送数据成功")
    else:
        return RestResponse(data=data, message="发送推送测试数据失败", detail=result[1], errCode=result[0])



def getDevice(user_id):
    devices = Device.objects.filter(user_id = user_id)
    return devices