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

@csrf_exempt
@api_view(['POST'])

def push_message(request):
    """
    消息推送测试接口
    """

    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')

    device_type = data.get('device_type')
    device_token = data.get('device_token')
    message = data.get('message')

    result = (0,'')

    if device_type == 'iOS':
        result = xgpush.push_ios_message(device_token = device_token, message = message)
    else:
        result = xgpush.push_android_message(device_token = device_token, title = '测试推送', message = message)

    if result[0] == 0:
        return RestResponse(data=data, message="发送推送测试数据成功")
    else:
        return RestResponse(data=data, message=result[1])