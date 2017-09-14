#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Thu Aug 24 2017
# File: serializers.py.py
# 
# Description: 
#

from rest_framework import serializers
from News.models import News


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ('id','url', 'title', 'source', 'pub_time', 'content', 'image_url')

    