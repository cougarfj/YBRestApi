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
from django.http import HttpResponse,JsonResponse
from rest_framework.request import QueryDict
from RestApi.response import RestResponse

@csrf_exempt


@api_view(['POST'])
def register(request):
    """
    注册设备
    """
    stream = request.read()
    data = QueryDict(stream, encoding='utf-8')
    serializer = DeviceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return RestResponse(data=serializer.data,message="注册设备成功")
    return RestResponse(data=None,message="注册设备失败",detail=serializer.errors)




@api_view(['POST'])
def push(request):
    """
    推送消息
    """
    
    return Response(data="OK",status=200)


