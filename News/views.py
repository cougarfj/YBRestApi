from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from rest_framework.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser
from rest_framework.renderers import JSONRenderer
from News.serializers import NewsSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.request import QueryDict
from RestApi.response import RestResponse
from News.models import News
import json

@csrf_exempt
@api_view(['GET'])
def list(request):
    """
    获取列表
    TODO: 参数检测，可否被转成Int
    """
    queryParams = request.query_params

    try:
        news_id = int(queryParams.get('news_id'))
        offset = int(queryParams.get('offset'))
        if news_id == None:
            return RestResponse(data=None, message="news_id is required", errCode = 1)
    
        if offset == None:
            offset = 20

        news_list = []
        if news_id == 0:
            news_list = News.objects.all().order_by('-id')[0:offset]
        else:
            news_list = News.objects.filter(id__lte = news_id).order_by('-id')[0:offset]
        
        for news in news_list:
            news.content = news.content[0:100]

        serializer = NewsSerializer(news_list, many=True)
        return RestResponse(data=serializer.data, message="获取列表数据成功")
    
    except:
        return RestResponse(data=None,message="参数类型错误",detail="param can not parse to int", errCode=2)
   


@csrf_exempt
@api_view(['GET'])
def detail(request):
    """
    获取详情
    """
    queryParams = request.query_params

    try:
        news_id = int(queryParams.get('news_id'))

        if news_id == None:
            return RestResponse(data=None, message="news_id is required", errCode = 1)

        try:
            news = News.objects.get(id=int(news_id))
            serializer = NewsSerializer(news, many=False)
            return RestResponse(data=serializer.data, message="获取记录成功")
        except News.DoesNotExist:
            return RestResponse(data=None,message="记录不存在",detail="news_id does not exsit", errCode=10)

    except:
        return RestResponse(data=None,message="参数类型错误",detail="param can not parse to int", errCode=2)