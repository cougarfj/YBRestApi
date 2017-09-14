#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Thu Sep 14 2017
# File: urls.py
# 
# Description: 
#

from django.conf.urls import url
from  News import views

urlpatterns = [
    url(r'^list',views.list),
    url(r'^detail',views.detail),
]