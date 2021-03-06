from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser
from rest_framework.renderers import JSONRenderer
from Push.serializers import DeviceSerializer,OpenWebPushMessageSerializer,OpenLiveRoomPushMessageSerializer,OpenTeamHallMessageSerializer
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
            response = self.get_paginated_response(serializer.data)
            return RestResponse(data=response.data,status=ResponseStatus.OK)

        serializer = self.get_serializer(queryset, many=True)
        
        return RestResponse(data=serializer.data,status=ResponseStatus.OK)


class DeviceFilterView(generics.GenericAPIView):
    """
    过滤列表
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    def get(self, request, *args, **kwargs):

        data = request.query_params
        is_delete = data.get('is_delete')
        after_time = data.get('after_time')
        device_type = data.get('device_type')

        if is_delete != None:
            self.queryset = self.queryset.filter(is_delete = is_delete)
        if device_type != None:
            self.queryset = self.queryset.filter(device_type = device_type)
        if after_time != None:
            try:
                self.queryset = self.queryset.filter(update_time__lte = after_time)
            except Exception as e:
                return RestResponse(data=data,status=ResponseStatus.PARAMS_ERROR,detail=str(e)) 
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        user_ids = None
        for device in queryset:
            if user_ids == None:
                user_ids =  device.user_id
            else:
                user_ids = user_ids +  "," + device.user_id
        
        return RestResponse(data=user_ids,status=ResponseStatus.OK)


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
            # xgpush.setTag(serializer.instance.user_id,serializer.instance.device_token,serializer.instance.device_type)
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





class PushCustomDataView(generics.GenericAPIView):
       
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            try:
                serializer_data = serializer.data
                # device_list = get_device_list(serializer.user_ids)
                # result = xgpush.push_message_to_multiple(device_token_list = device_list, message = serializer.alert, custom_data = serializer.custom_data)
                tags = get_tags(serializer.user_ids)
                result = xgpush.push_message_to_tags(tags,message=serializer.alert, custom_data=serializer.custom_data, send_time=serializer.send_time)
                if result[0] == OK:
                    return RestResponse(data=data, status=ResponseStatus.OK)
                else:
                    return RestResponse(data=data, status=ResponseStatus.PUSH_FAILED, detail=result[1])

            except Exception as e:
                return RestResponse(data=data,status=ResponseStatus.SERIALIZER_ERROR,detail=str(e))

        else:
            return RestResponse(data=data,status=ResponseStatus.SERIALIZER_ERROR,detail=serializer.errors)


class NotifyOpenWebView(PushCustomDataView):
    """
    通知设备打开指定网页
    """
    serializer_class = OpenWebPushMessageSerializer
    

    
class NotifyOpenLiveRoom(PushCustomDataView):
    """
    通知设备打开直播间
    """
    
    serializer_class = OpenLiveRoomPushMessageSerializer


class NotifyOpenTeamHall(PushCustomDataView):
    """
    通知设备打开团队首页
    """
    serializer_class = OpenTeamHallMessageSerializer







def get_tags(user_ids):
    user_id_list = user_ids.split(',')
    return user_id_list

def get_device_list(user_ids):
    user_id_list = user_ids.split(',')
    device_list = []
    for user_id in user_id_list:
        devices = Device.objects.filter(user_id=user_id)
        for device in devices:
            device_list.append(device.device_token) 
    return device_list
