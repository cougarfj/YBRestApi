from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import m3u8
from django.core.cache import cache,caches
import logging
import base64
# Create your views here.

logger = logging.getLogger('django')

@csrf_exempt
@api_view(['GET', 'POST'])
def query(request,hls):
    
    hls_str = str(base64.b64decode(hls),'utf-8')
    # cache_result =  cache.get(hls_str)
    cache_result = None

    if cache_result == None:
        try:
            m3u8_obj = m3u8.load(hls_str)
            if m3u8_obj.is_variant:
                for playlist in m3u8_obj.playlists:
                    sub_m3u8_obj = m3u8.load(playlist.uri)
            cache.set(hls_str,{"error":"0","mesage":"Ready"},60)
            logger.info(hls_str + ': Ready')
            return Response({"error":"0","mesage":"Ready"},status=status.HTTP_200_OK,headers={"Access-Control-Allow-Origin":"*"},content_type="application/json")
        except Exception as err:
            logger.info(hls_str + ': Not Ready')
            return Response({"error":"1","mesage":"Not Ready"},status=status.HTTP_200_OK,headers={"Access-Control-Allow-Origin":"*"},content_type="application/json") 
    else:
        logger.info(hls_str + ':Ready From Cache')
        return Response(cache_result,status=status.HTTP_200_OK,headers={"Access-Control-Allow-Origin":"*"},content_type="application/json")