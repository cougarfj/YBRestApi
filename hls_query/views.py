from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import m3u8

# Create your views here.

@csrf_exempt
def query(request):

    if request.method == 'GET':
        return HttpResponse(status=404)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        hls = data.get('hls')
        print(hls)
    try:
        m3u8_obj = m3u8.load(hls)
        if m3u8_obj.is_variant:
            for playlist in m3u8_obj.playlists:
                sub_m3u8_obj = m3u8.load(playlist.uri)
        return JsonResponse({"error":"0","mesage":"Ready"},status=200)
    except Exception as err:
        return JsonResponse({"error":"1","mesage":"Not Ready"},status=status.HTTP_200_OK)
